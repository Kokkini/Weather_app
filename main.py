from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=3aa596c4010eb1744783beac955c8e54')
	json_object = r.text
	return zipcode

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)