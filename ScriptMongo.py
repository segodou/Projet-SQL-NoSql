# On importe notre classe MongoClient
from pymongo import MongoClient

client = MongoClient()

# On vérifie que l'objet de class pymongo.mongo_client.MongoCLient a été créé
print(type(client))

# On se connecte à notre base de donnée et on affiche le contenu de l'entité workers choisi 

db = client.projet

result =  db.workers.find()
for document in result:
   print(document)

#5 NoSQL queries

# 1: Display the male workers.

result1 = db.workers.find({"gender" : "male"})
for document in result1:
   print(document)

# 2 : Count the number workers by gender.

result2 = db.workers.aggregate([{"$group": {"_id": "$gender", "total": { "$sum" : 1}}}])
for r in result2:
   print(r["total"], " ", r["_id"])


# 3 : Display the cities of the workers distinctly
db.workers.distinct("adress.city")


# 4 : Sort the workers by their city.
result4 = db.workers.find().sort([("adress.city", pymongo.ASCENDING)])
print(list(result4))

# 5 : Display the workers who live in the street "Rue des pucelles". 
result5 = db.workers.find({"adress.street" : "RUE DES PUCELLES"})
print(list(result5))