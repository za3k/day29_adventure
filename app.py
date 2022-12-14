#!/bin/python3
import flask, flask_login
from flask import url_for, request, render_template, redirect
from flask_login import current_user
from flask_sock import Sock
import collections, json, queue, random
from datetime import datetime
from base import app,load_info,ajax,DBDict,DBList,random_id,hash_id,full_url_for

# -- Info for every Hack-A-Day project --
load_info({
    "project_name": "Hack-An-Adventure",
    "source_url": "https://github.com/za3k/day29_adventure",
    "subdir": "/hackaday/adventure",
    "description": "A relaxing coloring book adventure. It is nice.",
    "instructions": "",
    "login": False,
    "fullscreen": True,
})

# -- Routes specific to this Hack-A-Day project --
adventures = DBDict("adventure")

@app.route("/")
def index():
    return render_template('index.html')

@ajax("/ajax/store")
def store(j):
    value = j["value"]
    key = hash_id(json.dumps(value))
    adventures[key] = value
    return {"key":key, "value": value}

@ajax("/ajax/get")
def get(json):
    key = json["key"]
    value = adventures.get(key)
    if value is None:
        return "", 404
    return {"key": key, "value":value}
