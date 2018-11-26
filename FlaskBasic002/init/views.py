from flask import Flask
from init import app

@app.route('/')
def home():
    return "Hello Again!"
