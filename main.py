from flask import Flask, render_template
import requests


app = Flask(__name__)

def get_posts(url):
    response = requests.get(url)
    response.raise_for_status
    return response.json()

blog_data = get_posts('https://api.npoint.io/43644ec4f0013682fc0d')

@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_data)

@app.route('/post/<id>')
def read_post(id):
    # sourced from https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
    blog_post = next((post for post in blog_data if post['id'] == int(id)), None)
    print(blog_post)
    return render_template('post.html', blog_post=blog_post)