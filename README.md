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
