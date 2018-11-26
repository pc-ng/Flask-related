# Flask-related
Some materials related to the lightweight Flask frameworks,  a "micro" framework which provides URL routing and page rendering for web applications.
Flask doesn't provide a page template engine. Other features can be obtained via Flask extensions. For example,  we can use extensions such as Jinja and Jade for templating.

## FlaskBasic001
__FlaskBasic001__ contains the boilerplate code created automatically by the visual studio.
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

Note: Flask is based on __WSGI (Web Server Gateway Interface)__.
It is a simple calling convetion for web servers to forward requests to web applications.

## FlaskBasic002
This project extends the __FlaskBasic001__ with structural formatting for further development with multiple views and templates.
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
Flask provides a convenient method to deliver a static file from code.
In __FlaskBasic004__, we added a static folder to hold all the static file including the "site.css" and "data.json".
Flask provides "send_static_file" function that can be called from code to refer to any file within the static folder.
For example, we can call the "data.json" file with the following:
```
@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')
```

Instead of defining the navigation link in each page, we can use a branding header and a navigation bar that provides the most important page links, popup menus, and so on.
The Jinja templating system provides two means for reusing specific elements across multiple templates:
1. includes: other page templates that are inserted at a specific place.
    - syntax: ```{% include <template_path> %}```
    - we can also use a variable to change the path dynamically in code
    - includes are typically used in the body of a page to pull in the shared template at a specific location on the page
2. inheritance: a shared base template that the referring template builds upon.
    - syntax: ```{% extends <template_path> %}```
    - it is commonly used to define a shared layout, nav bar, and other structures for an app's pages.
    - the referring templates need only to add or modify specific areas of the base template - blocks.
    
A base template delinaeates blocks using ```{% block <block_name> %}``` and ```{% endblock %}``` tags.
If a referring template then uses tags with the same block name, its block content overrides that of the base template.
