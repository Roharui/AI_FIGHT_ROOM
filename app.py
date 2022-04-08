import os
from dotenv import load_dotenv
from flask import Flask
from auth import login_required

load_dotenv(verbose=True)

app = Flask(__name__)

@app.route("/")
@login_required
def index(payload):
  return '<h1>Hello! %s</h1>' % payload["nickname"]

