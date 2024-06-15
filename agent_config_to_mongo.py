import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class AgentMongoDB:
    def __init__(self, collection, db_loc):
        self.db_loc = db_loc
        self.client = MongoClient(db_loc, server_api=ServerApi('1'))
        self.db = client['mydatabase']
        self.local_collection = self.collection
        self.server_collection = self.db['']


    def add(self, document):
        if not isinstance(document, dict):
            raise TypeError("document must be a dictionary")
        self.collection.insert_one(document)
        self.client.

    def query(self, query):
        if not isinstance(query, dict):
            raise TypeError("query must be a dictionary")
        return self.collection.find(query)

# import datetime

        # uri = f"mongodb+srv://swarms:swarms_password@cluster0.i3oqhnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # client = MongoClient(uri, server_api=ServerApi('1'))



    # uri = "mongodb+srv://swarms:swarms_password@cluster0.i3oqhnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # client = MongoClient(uri, server_api=ServerApi('1'))

    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)

    # db = client['mydatabase']
    # collection = db['agents']

    # # Ask for user input
    # name = input("Enter agent name: ")
    # response = input("Enter agent response: ")
    # preference = input("Enter agent preference: ")
    # time = datetime.datetime.now()

    # # Create a document
    # agent_data = {
    #     "name": name,
    #     "time": time,
    #     "response": response,
    #     "preference": preference
    # }

    # # Insert document into collection
    # result = collection.insert_one(agent_data)
    # print(f"Agent data inserted with id: {result.inserted_id}")