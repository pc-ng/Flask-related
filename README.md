# Flask-related
Some materials related to the lightweight Flask frameworks,  a "micro" framework which provides URL routing and page rendering for web applications.
Flask doesn't provide a page template engine. Other features can be obtained via Flask extensions. For example,  we can use extensions such as Jinja and Jade for templating.

## FlaskBasic001
FlaskBasic001 contains the boilerplate code created automatically by the visual studio.
The "app.py" contains the main code for URL routing and page rendering.
The function to a URL route provides the resource identified by the URL.
We define routes using Flask's decorator, i.e., @app.route('/').
In general, we can have many different decorators for the same function but serves multiple routes.

For example, 
```
@app.route('/')
@app.route('/hello')
@app.route('hello/<name>?message=<msg>'
```

Note: Flask is based on WSGI (Web Server Gateway Interface).
It is a simple calling convetion for web servers to forward requests to web applications.

## FlaskBasic002
This project extends the "FlaskBasic001" with structural formatting for further development with multiple views and templates.
In particular, a folder "init" is created to hold the app object and views.
The "views.py" contatins the page rendering code by importing the app object.
We renamed the root python files to "runserver.py", which defines the execution of the web application.

In "views.py", we uses inline HTML to create dynamic content, i.e.,
```
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    html_content = "<html><head><title>Hello Flask</title></head><body>"
    html_content += "<strong>Hello Flask!</strong> on " + formatted_now
    html_content += "</body></html>"

    return html_content
```

## FlaskBasic003
Instead of using inline HTML, this project exploit the template for page rendering.
In particular, an "index.html" is created in the templates folder. 
A placeholder is used to accept the content defined by the function in "views.py", i.e.,
```
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <strong>{{ message }}</strong>{{ content }}
    </body>
</html>
```

We need to import the render_template from flask.
Note that the render_template will automatically skip the inline HTML content.
In other words, we can't have inline HTML content when using render_template.
Instead, every HTML styling is maintained with a separate markup file.

## FlaskBasic004


