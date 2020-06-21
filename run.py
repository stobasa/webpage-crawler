import os
import json
from flask import Flask, request, redirect, url_for, jsonify
from api.crawler import merge_year_data, open_json

app = Flask(__name__)

all_links = open_json("all_data.json")

@app.route('/', methods=['POST', "GET"])
def home():
    return jsonify({"Get all date": "/all", "Get Single Date": "/getdate"})

@app.route('/all', methods=['GET'])
def Get_all():
    #all_links = merge_year_data()
    return jsonify(all_links)

@app.route('/getdate/<date>', methods=['GET'])
def Get_date(date):
    date = date.replace("-", "/")
    #all_links = merge_year_data()
    dates = json.load(all_links)
    date_link = dates[date]
    return jsonify({date : dates[date_link]})




if __name__ == "__main__":
    app.run(debug=True)
