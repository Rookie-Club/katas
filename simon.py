
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        uploaded_file  = request.files['file']
        if uploaded_file.filename == '':
            return redirect('/upload')
        uploaded_file.save('uploaded_file')
        return redirect('/')

    if request.method == 'GET':
        return render_template('upload.html')

@app.route("/references")
def references():
    return render_template('references.html')

@app.route("/generate")
def generate():
    uploaded_file = open('uploaded_file', 'r')
    uploaded_content = uploaded_file.read()
    return render_template('generate.html', uploaded_content = uploaded_content)

if __name__ == "__main__":
    app.run()
