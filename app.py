from flask import Flask, render_template, jsonify 

app = Flask(__name__)

ARTICLES = [
  {
    "id": 1,
    "title": "Skylar Asoka",
    "category": "Personal Website",
    "content": "A list of websites I have created"
  },
  {
    "id": 2,
    "title": "Lang Tengah Island",
    "category": "Travel Website",
    "content": "Tours for Lang Tengah Island"
  },
  {
    "id": 3,
    "title": "Merang Jetty",
    "category": "Travel Website",
    "content": "Website to book boat tickets"
  },
  {
    "id": 4,
    "title": "Lang Tengah Island",
    "category": "Travel Website",
    "content": "Try & Error"
  },
  {
    "id": 5,
    "title": "My Note",
    "category": "Create Note, Delete Note",
    "content": "Try & Error"
  },
  {
    "id": 6,
    "title": "Microblog",
    "category": "Microblog",
    "content": "Learning flask framework"
  } 
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=ARTICLES, owner="Skylar Asoka")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(ARTICLES)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/greet')
def greet():
    return render_template('greet.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
