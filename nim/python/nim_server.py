from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "2x+cool"

@app.route("/jouer")
def jouer():
    return "cool"

if __name__ == "__main__":
    app.run()
