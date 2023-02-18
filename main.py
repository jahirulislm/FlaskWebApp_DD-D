from flask import Flask, render_template

# creating instance of class, __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


#route() decorator to tell Flask what URL should trigger our function
@app.route("/")
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
