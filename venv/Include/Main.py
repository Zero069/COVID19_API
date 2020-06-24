from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    country = "turkey"
    return country_covid_cases(country)


def country_covid_cases(country):
    request = requests.get("https://api.covid19api.com/country/" + country)  # Concatenates "country" with url.
    return jsonify(request.text)

def global_summmary():
    request = requests.get("https://api.covid19api.com/summary")
    return request


if __name__ == '__main__':
    app.run(debug=True)
