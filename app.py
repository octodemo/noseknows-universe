from flask import Flask, render_template
from flask import Flask, request
from flask_cors import cross_origin
from recommend_fragrance import recommend_perfumes

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# create a route that returns perfume recommendations based on the user input
# the function accepts 1 param, fav_perfumes, which is a list of the user's favorite perfumes

@app.route('/api/recommend', methods=['POST'])
@cross_origin()
def recommend():
    # check if 'fav_perfumes' key is in the request's JSON
    if 'fav_perfumes' not in request.json:
        return {"error": "'fav_perfumes' key is missing from request"}, 400

    # get the user's favorite perfumes from the request
    fav_perfumes = request.json['fav_perfumes']

    # validate 'fav_perfumes' input
    if not isinstance(fav_perfumes, list) or not all(isinstance(i, str) for i in fav_perfumes):
        return {"error": "'fav_perfumes' must be a list of strings"}, 400

    # get perfume recommendations
    recs = recommend_perfumes(fav_perfumes)

    # return recommendations in a consistent format
    return {"recommendations": recs}, 200

if __name__ == '__main__':
    app.run(debug=True)