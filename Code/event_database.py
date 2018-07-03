"""
connect to database and inert data to database
"""
import sqlite3
import csv
import os

db = "event.db"

# Path Settings
work_path = '/Users/dangchong/Documents/Github/CodingTask/Code'
db_path = 'event.db'
data_path = 'event.csv'

# set database path
os.chdir(work_path)
conn = sqlite3.connect(db_path)
c = conn.cursor()

# create a table and save it in the database
c.execute(""" CREATE TABLE event 
                                    (pd_index,
                                    id,
                                    title,
                                    description,
                                    link,
                                    categories_id,
                                    categories_title,
                                    geometries_coordinates,
                                    geometries_date,
                                    geometries_type,
                                    sources_id,
                                    sources_url
                                    ); """)

# event data path
csvfile = open(data_path, 'rU')
fieldnames = ['pd_index',
              'id',
              'title',
              'description',
              'link',
              'generic_name',
              'categories_id',
              'categories_title',
              'geometries_coordinates',
              'geometries_date',
              'geometries_type',
              'sources_id',
              'sources_url']
reader = csv.DictReader(csvfile, fieldnames=fieldnames)
next(reader)
for row in reader:
    c.execute("INSERT INTO event(pd_index, "
              "id, "
              "title, "
              "description, "
              "link, "
              "categories_id, "
              "categories_title, "
              "geometries_coordinates, "
              "geometries_date, "
              "geometries_type, "
              "sources_id, "
              "sources_url) "
              "VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",
              (row['pd_index'],
               row['id'],
               row['title'],
               row['description'],
               row['link'],
               row['categories_id'],
               row['categories_title'],
               row['geometries_coordinates'],
               row['geometries_date'],
               row['geometries_type'],
               row['sources_id'],
               row['sources_url']))
conn.commit()
conn.close
