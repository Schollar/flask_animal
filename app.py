from flask import Flask, request, Response
import json
import dbhandler as dbh
from flask_cors import CORS, cross_origin
db = dbh.dbInteraction()
app = Flask(__name__)
CORS(app)


# GET REQUEST stores animal list being returned from get_animals function, then we dump it to json, and return our response with the json we just converted.


@app.get('/animals')
def animals():
    animals_list = db.get_animals()
    animals_json = json.dumps(animals_list, default=str)
    return Response(animals_json, mimetype="application/json", status=200)

# POST request that takes in data with the request.json, then send the data to our db handler add animal function


@app.post('/animals')
def add_animal():
    animal_name = request.json['name']
    animal_desc = request.json['description']
    if(db.add_animal(animal_name, animal_desc)):
        return Response("You've successfully added an animal", mimetype="plain/text", status=200)
    else:
        return Response("Something went wrong adding an animal", mimetype="plain/text", status=400)

# PATCH request that takes in animal name, new name, and new description data with the request.json, then send the data to our db handler changeanimal function


@app.patch('/animals')
def change_animal():
    animal_name = request.json['name']
    new_name = request.json['new_name']
    new_description = request.json['description']
    if(db.change_animal(animal_name, new_name, new_description)):
        return Response("You've successfully changed an animal", mimetype="plain/text", status=200)
    else:
        return Response("Something went wrong changing the animal", mimetype="plain/text", status=400)

# DELETE request that takes in animal name with the request.json, then send the data to our db handler delete animal function


@app.delete('/animals')
def remove_animal():
    animal_name = request.json['name']
    db.delete_animal(animal_name)
    return Response("You've successfully deleted an animal", mimetype="plain/text", status=200)


app.run(debug=True)
