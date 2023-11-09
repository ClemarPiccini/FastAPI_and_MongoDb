from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:OopxqEC5WowzHn3k@cluster0.jccd19i.mongodb.net/")

databases = client.list_databases()
