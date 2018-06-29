import requests
import os
import pandas as pd
from pandas.io.json import json_normalize

save_path = '/Users/dangchong/Desktop/coding_task'

# get data from url
url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events"
json_data = requests.get(url).json()

# normalize event data
df = json_normalize(json_data['events'])

# flatten DataFrame with some columns as json
categories = json_normalize(data=json_data['events'], record_path='categories').add_prefix('categories_')
sources = json_normalize(data=json_data['events'], record_path='sources').add_prefix('sources_')
geometries = json_normalize(data=json_data['events'], record_path='geometries').add_prefix('geometries_')

# concat the DataFrame
df = df[['id', 'title', 'description', 'link']].join([categories, sources, geometries])

# select wildfires, severe storms, and landslides from the past month
Wildfires = df.loc[df['categories_title'] == 'Wildfires']
Severe_Storms = df.loc[df['categories_title'] == 'Severe Storms']
Landslides = df.loc[df['categories_title'] == 'Landslides']
frames = [Wildfires, Severe_Storms, Landslides]
df = pd.concat(frames)

# select data from the past month
df_time = df['geometries_date'].str.contains('2018-06')
df_result = df[df_time]

# write csv file, setting your path
df_result.to_csv(os.path.join(save_path, 'event.csv'))
