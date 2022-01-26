# Flask implements many of the things we need for microservices
import imp
from flask import Flask, render_template # may need to pip install flask

import json
from memory_profiler import profile

# we begin by declaring our Flask server
app = Flask(__name__) # convention
# declare the root path
@app.route('/') # this is the ROUTE to the ROOT of our application
def root():
    # we can declare an html response
    content = '''
    <h1>we are at the root of this service</h1>
    <a href='/hello'>greeting</a>
    '''
    return content

# we can customize the headers sent with any response
#                           will be JSON  CORS header cross-origin-resource-sharing
my_header = {'content-type':'text.json', 'access-allow-origin':'127.0.0.1'}

# these routes all handle 'GET' requests
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None): # default name is unspecified
    # return '<h2>Hello from flask</h2>'
    return render_template('greeting.html', name=name)

# we can use Flask to provide data to other microservices
@app.route('/data')
@app.route('/data/<age>') # here we can provide a parameter on the URL for 'age'
@app.route('/data/<age>/<name>') # two parameters, 'age' and 'name'
def data(age=92, name='Deidre'): # here we have default values
    struct = {'age':age, 'name':name, 'member':True}
    # struct_j = json.dumps(struct) # we have a JSON version of our data
    # return struct_j
    return struct # modern Flask will convert response to JSON

# we need to get our server running
@profile # we see the profile once we quit the server
def main():
    app.run(host='127.0.0.1') # localhost

if __name__ == '__main__':
    main()


