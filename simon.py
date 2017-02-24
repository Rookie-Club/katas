
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploaded_file')
        return redirect('/')

    if request.method == 'GET':
        return render_template('upload.html')

@app.route("/references")
def references():
    return render_template('references.html')

@app.route("/generate")
def generate():
    f = open('uploaded_file', 'r')
    content_f = f.read()
    return render_template('generate.html', content_f = content_f)

if __name__ == "__main__":
    app.run()
