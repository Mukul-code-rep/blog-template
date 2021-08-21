from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

data = requests.get('https://api.npoint.io/4af156202f984d3464c3').json()
posts = []
for post in data:
    posts.append(Post(id=post["id"], subtitle=post["subtitle"], title=post["title"], body=post["body"]))


@app.route('/')
def home():
    return render_template("index.html",
                           all_posts=posts)


@app.route('/blog/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
