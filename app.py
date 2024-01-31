from flask import Flask, render_template, jsonify 

app = Flask(__name__)

ARTICLES = [
  {
    "id": 1,
    "title": "From Non-Tech to Tech",
    "category": "Personal Development",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 2,
    "title": "Why I Learn to Code?",
    "category": "Programming",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 3,
    "title": "What Causes Monsoon?",
    "category": "Curiosity Chronicles",
  },
  {
    "id": 4,
    "title": "Lang Tengah Island",
    "category": "Projects",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
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
