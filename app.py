import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')

def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7695e0fb88f7f35ea24ebbdea052ca90'
    city = 'San Fransisco'

    responce = requests.get(url.format(city)).json()
    print(responce)
    return render_template('weather.html')

