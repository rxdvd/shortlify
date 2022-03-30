from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values('.env')

def init():
  client = MongoClient(config['CONN_STRING'])
  return client

if __name__ == "__main__":
  client = init()
  print(list(client.shortlify.url_data.find()))
