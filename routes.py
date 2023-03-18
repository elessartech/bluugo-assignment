import json
import models
from app import app
from flask import render_template, redirect, request


@app.route("/", methods=["GET", "POST"])
def index():
    rejections = models.get_rejections()
    return render_template("index.html", rejections=rejections)


@app.route("/filter")
def filter():
    searchbar_val = request.args.get("searchbar_val")
    filtered_rejections = models.filter_rejections(searchbar_val)
    return render_template("filter.html", rejections=filtered_rejections)


@app.route("/vehicle-data", methods=["POST"])
def vehicle_data():
    vehicle_data_input_file = request.files["vehicle-data-input"]
    vehicle_data = json.load(vehicle_data_input_file)
    for data_obj in vehicle_data:
        model_year = int(data_obj["model_year"])
        make = data_obj["make"]
        model = data_obj["model"]
        rejection_percentage = float(data_obj["rejection_percentage"].replace(",", "."))
        reason_1 = data_obj["reason_1"]
        reason_2 = data_obj["reason_2"]
        reason_3 = data_obj["reason_3"]
        models.save_rejection(
            model_year, make, model, rejection_percentage, reason_1, reason_2, reason_3
        )
    return redirect("/")
