from flask import Flask, render_template

app = Flask(__name__)

ARTICLES = [
  {
    "id": 1,
    "title": "Island Tourism",
    "author": "John Smith",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 2,
    "title": "Fishing Trip",
    "author": "Jane Doe",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 3,
    "title": "Skiing Trip",
    "author": "Bob Johnson",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 4,
    "title": "Hiking Trip",
    "author": "Sarah Lee",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  } 
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=ARTICLES, owner="Han Asoka")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
