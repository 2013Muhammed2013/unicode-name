from flask import Flask
from unicodedata import name
app=Flask(__name__)
@app.route("/<string:x>")
def f(x):
	return name(x, "Undefined")