from flask import Flask 
app = Flask(__name__)

#Basic routing
@app.route('/')
def index():
    return "Index page"

@app.route('/hello')
def hello_world():
    return "Hello, World!"

#Routing with variable rules
@app.route('/user/<username>')
def show_user_profile(username):
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

#Unique/Canonical URLs
@app.route('/projects/')
def projects():
    #note trailing slash
    return 'The project page'

@app.route('/about')
def about():
    #not no trailing slash
    return 'The about page'





