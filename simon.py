
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload")
def upload():
    return "on est sur la page upload"

@app.route("/references")
def references():
    return "on est sur la page references"

@app.route("/generate")
def generate():
    return "on est sur la page generate"

if __name__ == "__main__":
    app.run()
