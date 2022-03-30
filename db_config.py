from pymongo import MongoClient

def init():
  CONN_STRING = "mongodb+srv://hamza:King2030@cluster0.zyax5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
  client = MongoClient(CONN_STRING)
  return client

if __name__ == "__main__":
  client = init()
  print(list(client.shortlify.url_data.find()))
