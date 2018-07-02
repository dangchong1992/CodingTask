import requests
import os
import pandas as pd
from pandas.io.json import json_normalize

# Please change 'save_path' to your local path
save_path = '/Users/dangchong/Documents/Github/CodingTask/Code'

# get data from url
url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events"
json_data = requests.get(url).json()

# normalize event data
df = json_normalize(json_data['events'])

# flatten categories with some columns as json and then combine with other columns
categories = json_normalize(data=json_data['events'], record_path='categories').add_prefix('categories_')
df_add_categories = df[['id', 'title', 'description', 'link']].join(categories)

# flatten geometries
# Because some event with multiple geometries, we can use eventID to distinguish them
geometries = json_normalize(data=json_data['events'], record_path='geometries', meta=['id']).add_prefix('geometries_')
df_add_geometries = pd.merge(df_add_categories, geometries, left_on='id', right_on='geometries_id')

# flatten sources
# 'id' in source and 'id' in event will cause conflict
# But link is unique, We can use link to distinguish them
sources = json_normalize(data=json_data['events'], record_path='sources', meta='link').add_prefix('sources_')
df_final = pd.merge(df_add_geometries, sources, left_on='link', right_on='sources_link')
# Because 'geometries_id' is same to 'id' and 'sources_link' same to 'link', delete them
df = df_final.drop(['geometries_id', 'sources_link'], axis=1)

# select wildfires, severe storms, and landslides from the past month
wildfires = df.loc[df['categories_title'] == 'Wildfires']
severe_storms = df.loc[df['categories_title'] == 'Severe Storms']
landslides = df.loc[df['categories_title'] == 'Landslides']
df_select = pd.concat([wildfires, severe_storms, landslides])

# select data from the past month
df_time = df_select['geometries_date'].str.contains('2018-06')
df_result = df_select[df_time]

# write csv file, setting your path
df_result.to_csv(os.path.join(save_path, 'event.csv'))



