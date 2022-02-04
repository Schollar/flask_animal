from flask import Flask, request, Response
import json
app = Flask(__name__)


@app.get('/animals')
def animals():
    animals_json = json.dumps(animals_list, default=str)
    return Response(animals_json, mimetype="application/json", status=200)


@app.post('/animals')
def add_animal():
    user_animal = request.json['animal']
    animals_list.append(user_animal)
    return Response("You've successfully added an animal", mimetype="plain/text", status=200)


@app.patch('/animals')
def change_animal():
    animals_list[1] = "Large Dog"
    return Response("You've successfully changed an animal", mimetype="plain/text", status=200)


@app.delete('/animals')
def remove_animal():
    animals_list.remove("Cat")
    return Response("You've successfully deleted an animal", mimetype="plain/text", status=200)


animals_list = ["Cat", "Dog", "Gorilla"]


app.run(debug=True)
