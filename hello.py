from flask import Flask, url_for
from flask import request 
from flask import render_template

app = Flask(__name__)

#Basic routing
@app.route('/')
def index():
    return "Index page"

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html',name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

#Routing with variable rules
@app.route('/user/<username>')
def profile(username):
    #show the user-profile for that user
    return 'User: %s' % username

@app.route('/post/<int:post_id>')
def show_post_(post_id):
    #show post with given integer id
    return 'Post: %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show subpath after path
    return 'Subpath: %s' % subpath

"""note: converter types: string, int, float
                            path, uuid   """

def do_the_login():
    return "I am the login"

def show_the_login_form():
    return "I am the login form"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next="/"))
    print(url_for('profile', username='John Doe'))





