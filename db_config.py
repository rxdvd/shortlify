def get_collection():
  import pymongo
  from pymongo import MongoClient

  CONN_STRING = "mongodb+srv://hamza:King2030@cluster0.zyax5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

  client = MongoClient(CONN_STRING)

  return client["url_data"]

if __name__ == "__main__":
  import json
  collection = get_collection()
