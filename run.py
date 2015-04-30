# coding: latin1
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

# Routes
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)