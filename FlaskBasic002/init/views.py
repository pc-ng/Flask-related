from datetime import datetime
from flask import Flask
from init import app

@app.route('/')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    html_content = "<html><head><title>Hello Flask</title></head><body>"
    html_content += "<strong>Hello Flask!</strong> on "
    html_content += formatted_now
    html_content += "</body></html>"

    return html_content
