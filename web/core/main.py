# @__author__ == Isotone

#Packages
from flask import Flask #session, redirect, render_template, request
from database import *
from routes import *


#Globals
App = Flask(__name__)

def main(port):
	App.run(port=port)

if __name__ == '__main__':
	App.run(debug=True)