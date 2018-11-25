# Flask-related
Some materials related to the lightweight Flask frameworks, which is a "micro" framework for web applications, providing URL routing and page rendering.
Other features can be obtained via Flask extensions. For example, Flask doesn't provide a page template engine. Templating is provided by extensions such as Jinja and Jade.

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

