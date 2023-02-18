from flask import Flask, render_template
from flask import jsonify

# creating instance of class, __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# creating list
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Banglades',
    'salary': 'Tk. 10000'
  },
  {
    'id': 2,
    'title': 'Ux Analyst',
    'location': 'Bangladess',
    'salary': 'Tk. 12000'
  },
  {
    'id': 3,
    'title': 'front end dev',
    'location': 'USA',
    'salary': 'dollars. 10000'
  },
  {
    'id': 4,
    'title': 'Back end dev',
    'location': 'UK',
    'salary': 'UR. 10000'
  },
  {
    'id': 5,
    'title': 'FUll stack',
    'location': 'EU',
    'salary': 'Eu 10000'
  },
]


#route() decorator to tell Flask what URL should trigger our function
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, c_name='Jahirul Islam')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
