"""
connect to database and inert data to database
"""
import sqlite3
import csv
import os

db = "event.db"

# Path Settings
work_path = '/Users/dangchong/Desktop/coding_task'
db_path = '/Users/dangchong/Desktop/coding_task/event.db'
data_path = '/Users/dangchong/Desktop/coding_task/event.csv'

# Create a connection to the SQLite database
conn = sqlite3.connect(db)
c = conn.cursor()

# create a table and save it in the database
c.execute(""" CREATE TABLE event    (id,
                                    title,
                                    description,
                                    link,
                                    categories_id,
                                    categories_title,
                                    sources_id,
                                    sources_url,
                                    geometries_coordinates,
                                    geometries_date,
                                    geometries_type
                                    ); """)


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


# insert data to DB, need to set your work_path and db_path
os.chdir(work_path)
conn = sqlite3.connect(db_path)
c = conn.cursor()

# create a table and save it in the database
c.execute(""" CREATE TABLE event 
                                    (id,
                                    title,
                                    description,
                                    link,
                                    categories_id,
                                    categories_title,
                                    sources_id,
                                    sources_url,
                                    geometries_coordinates,
                                    geometries_date,
                                    geometries_type
                                    ); """)

# event data path
csvfile = open(data_path, 'rU')
fieldnames = ['id',
              'title',
              'description',
              'link',
              'generic_name',
              'categories_id',
              'categories_title',
              'sources_id',
              'sources_url',
              'geometries_coordinates',
              'geometries_date',
              'geometries_type']
reader = csv.DictReader(csvfile, fieldnames=fieldnames)
for row in reader:
    c.execute("INSERT INTO event(id, "
              "title, "
              "description, "
              "link, "
              "categories_id, "
              "categories_title, "
              "sources_id,sources_url, "
              "geometries_coordinates, "
              "geometries_date, "
              "geometries_type) "
              "VALUES (?,?,?,?,?,?,?,?,?,?,?);",
              (row['id'],
               row['title'],
               row['description'],
               row['link'],
               row['categories_id'],
               row['categories_title'],
               row['sources_id'],
               row['sources_url'],
               row['geometries_coordinates'],
               row['geometries_date'],
               row['geometries_type']))
conn.commit()
conn.close
