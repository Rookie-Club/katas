
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/references")
def references():
    return render_template('references.html')

@app.route("/generate")
def generate():
    return render_template('generate.html')

if __name__ == "__main__":
    app.run()
