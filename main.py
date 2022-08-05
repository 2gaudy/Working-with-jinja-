from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    today = dt.datetime.now()

    year = today.year
    name = "Austin Grant"
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, CURRENT_YEAR=year, CREATOR=name)


@app.route("/guess/<string:name>")
def guess(name):
    params_age = {
        "name": name,
        "country_id": "US"
    }

    params_gender = {
        "name": name,
        "country_id": "US"
    }

    age_response = requests.get(url="https://api.agify.io", params=params_age)
    age = age_response.json()
    name = name.title()

    gender_response = requests.get(url="https://api.genderize.io", params=params_gender)
    gender = gender_response.json()

    return render_template("guess.html", name=name, gender=gender["gender"], age=age["age"])

@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
