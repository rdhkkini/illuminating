import urllib3
import os
import json
import facebook
import requests
from pymongo import MongoClient

# Mongo Data Base
client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
db = client['test-database']

collection = db.test_collection
collection = db['test-collection']


# FACEBOOK APP DETAILS
access_token = "EAABeVXKMg0wBAOIVi3VqciICflGXQJAVoEsFnZBOIBTRZC1aXAjA5ZCj7ep6nuI14enbialZC3qngLwZCcMQ1ygtH218OxKeMaGjab3NEBEZCSk9TLL8fl0GRjDZCZBogGxEwSB9QEQffrB4nAZBIpVAytmtyRZBYfkRIZD"
app_ID = "449824012079469"
app_Secret = "fd931422fd2cc5cd89db24c832ba25f5"
user = ['DonaldTrump','BillGates','narendramodi','Federer']
fields ="id,app_id,fan_count,attire,best_page,bio"
fields_posts ="posts{id,message,created_time,description,updated_time,shares.limit(10).summary(true),likes.limit(10).summary(true)}"
fields_comments = "posts{comments{comment_count,created_time,from,id,reactions,user_likes}}"
since = "2015-01-20T18:44:30+0000"
until = "2017-05-20T18:44:30+0000"



# CONSTRUCT THE URL (GRAPH API)
facebook_base = "https://graph.facebook.com/v2.10"
for i in range (0,4):
	node = "/"+user[i]
	access_parameter = "/?access_token=%s" %access_token
	hiddden ="&include_hidden=true"
	since ="&since=%s" %since
	until = "&until=%s" %until
	fields_parameter = "&fields=%s" %fields

	url = facebook_base+node+access_parameter+hiddden+since+until+fields_parameter
	print(node)
	response = requests.get(url)
	feeds = response.json()
	print(feeds)

	#feeds = db.feeds
	#feeds_id = feeds.insert_one(feeds).inserted_id
	#feeds_id
	#db.collection_names(include_system_collections=False)


# CONSTRUCT URL FOR POSTS
for i in range (0,4):
	node = "/"+user[i]
	access_parameter = "/?access_token=%s" %access_token
	hiddden ="&include_hidden=true"
	since ="&since=%s" %since
	until = "&until=%s" %until
	fields_parameter = "&fields=%s" %fields_posts

	url = facebook_base+node+access_parameter+hiddden+since+until+fields_parameter
	print(node)
	response = requests.get(url)
	print(response.json())

# CONSTRUCT URL FOR COMMENTS
for i in range (0,4):
	node = "/"+user[i]
	access_parameter = "/?access_token=%s" %access_token
	hiddden ="&include_hidden=true"
	since ="&since=%s" %since
	until = "&until=%s" %until
	fields_parameter = "&fields=%s" %fields_comments

	url = facebook_base+node+access_parameter+hiddden+since+until+fields_parameter
	print(node)
	response = requests.get(url)
	print(response.json())


