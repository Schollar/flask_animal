from flask import Flask, request, Response
import json
import dbhandler as dbh
db = dbh.dbInteraction()
app = Flask(__name__)

# GET REQUEST stores animal list being returned from get_animals function, then we dump it to json, and return our response with the json we just converted.


@app.get('/animals')
def animals():
    animals_list = db.get_animals()
    animals_json = json.dumps(animals_list, default=str)
    return Response(animals_json, mimetype="application/json", status=200)


@app.post('/animals')
def add_animal():
    animal_name = request.json['name']
    animal_desc = request.json['description']
    db.add_animal(animal_name, animal_desc)
    return Response("You've successfully added an animal", mimetype="plain/text", status=200)


@app.patch('/animals')
def change_animal():
    animal_name = request.json['name']
    new_name = request.json['new_name']
    new_description = request.json['description']
    db.change_animal(animal_name, new_name, new_description)
    return Response("You've successfully changed an animal", mimetype="plain/text", status=200)


@app.delete('/animals')
def remove_animal():
    animal_name = request.json['name']
    db.delete_animal(animal_name)
    return Response("You've successfully deleted an animal", mimetype="plain/text", status=200)


app.run(debug=True)
