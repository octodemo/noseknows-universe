from flask import Flask, render_template
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/api/sample_perfumes')
@cross_origin()
def sample_perfumes():
    with open('data/sample_perfumes.csv', 'r') as file:
        sample_perfumes = file.read().splitlines()
    return {"sample_perfumes": sample_perfumes}

if __name__ == '__main__':
    app.run(debug=True)