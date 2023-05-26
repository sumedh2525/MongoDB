# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use
# MongoDB over SQL databases?
# Ans:
# MongoDB is a non-relational document database that provides a flexible data model for storing data.
#  It is a popular choice for applications that need to store large amounts of data, such as social media, e-commerce, and gaming.
#Non-relational databases, also known as NoSQL databases, are a type of database that does not use the traditional relational model. 
# Relational databases store data in tables, with each table having a set of columns and rows. Non-relational databases, on the other hand, store data in a variety of formats, including documents, key-value pairs, and graphs.
# MongoDB is a document database, which means that data is stored in documents that are similar to JSON objects. This makes it easy to store and query data that is not well-suited for a relational database, such as documents 
# with nested data or documents that are frequently updated.





# Q2. State and Explain the features of MongoDB.
# Ans:
#Flexible schema: MongoDB does not require a rigid schema for its documents. This makes it easy to add new fields to documents or change the structure of existing documents.
#High performance: MongoDB is designed for high performance, which makes it a good choice for applications that need to process large amounts of data quickly.
#Scalability: MongoDB can be scaled horizontally, which means that you can add more servers to increase the capacity of your database.
#Replication: MongoDB supports replication, which means that your data can be stored on multiple servers. This makes it possible to keep your data available even if one server fails.
#Security: MongoDB supports a variety of security features, such as authentication, authorization, and encryption.
#Community: MongoDB has a large and active community of users and developers. This means that there is a lot of support available for MongoDB, and there are many tools and resources available to help you use MongoDB.




#Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

import pymongo

# Create a connection to Mongodb
client = pymongo.MongoClient("mongodb://localhost:277")

# create a database
db = client["my_database"]
# create a collection
collection = db["my_collection"]
# insert a document in collection
document = {"name":"Sumedh" , "age": 19}
collection.insert_one(document)
documents  = collection.find()
print(document)






#Q4. Using the database and the collection created in question number 3, write a code to insert one record,
#and insert many records. Use the find() and find_one() methods to print the inserted record.

#Ans:
#insert many documents
documents = [{"name":"sumedh","age": 18},
{"name":"kittu","age": 15}]

collection.insert_many(documents)
documents = collection.find()
for document in documents:
    print(document)
document = collection.find_one()
print(document)







#Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to
#demonstrate this.
import pymongo

client = pymongo.MongoClient("mongo://localhost:277")

db = client["my_database"]
collection = db["my_collection"]
documents = collection.find({"name":"kittu"})
for document in documents:
    print(document)






#Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
#Ans:
db.mycol.find().sort({title: -1})
db.mycol.find().sort({title: -1, author: 1})
db.mycol.find({title: "MongoDB"}).sort({author: 1})





#Q7. Explain why delete_one(), delete_many(), and drop() is used.
#Ans:
# delete_one() deletes a single document from a collection.
# delete_many() deletes multiple documents from a collection.
# drop() deletes all documents from a collection.

# BY USING ABOVE CODES
db.mycol.delete_many({title : "MongoDB"})
db.mycol.drop()
