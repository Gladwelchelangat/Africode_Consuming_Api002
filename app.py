from flask import Flask, render_template
import requests

app = Flask(__name__)
BASE_URL = 'https://jsonplaceholder.typicode.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def get_posts():
    posts = requests.get(f"{BASE_URL}/posts").json()
    return render_template('posts.html', posts=posts)

@app.route('/comments')
def get_comments():
    comments = requests.get(f"{BASE_URL}/comments").json()
    return render_template('comments.html', comments=comments)

@app.route('/albums')
def get_albums():
    albums = requests.get(f"{BASE_URL}/albums").json()
    return render_template('albums.html', albums=albums)

@app.route('/photos')
def get_photos():
    photos = requests.get(f"{BASE_URL}/photos").json()
    return render_template('photos.html', photos=photos)

@app.route('/todos')
def get_todos():
    todos = requests.get(f"{BASE_URL}/todos").json()
    return render_template('todos.html', todos=todos)

@app.route('/users')
def get_users():
    users = requests.get(f"{BASE_URL}/users").json()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
