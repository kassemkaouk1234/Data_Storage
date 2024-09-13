import pymongo
import json


#connect to MongoDB:
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Al_Mayadeen"]
collection = db["articles"]

#load and insert JSON data:
with open(r'C:\Users\okay\Desktop\pythonProject2\.venv\output\articles_2024_8.xml.json','r',encoding='utf-8' ) as f:
    data = json.load(f)
    print(f"Data to insert: {data}")  # Check the data being read
    collection.insert_many(data)
    print("Data inserted successfully.")