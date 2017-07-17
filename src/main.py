from flask import Flask, render_template
from pymongo import MongoClient

## Creamos la app
app = Flask(__name__)

## Creamos el cliente MongoDB (luego podremos accceder client.[nombre de dataset])
client = MongoClient()

@app.route('/')
def show_map():
    return render_template('map.html')
