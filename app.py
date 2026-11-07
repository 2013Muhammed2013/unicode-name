from flask import Flask
from flask_cors import CORS
from unicodedata import name
app=Flask(__name__)
CORS(app)
@app.route("/<string:x>")
def f(x):
	return name(x, "Undefined")
