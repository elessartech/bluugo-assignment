import json
import queries
from app import app
from flask import render_template, redirect, request


@app.route("/")
def index():
    vehicles = queries.get_vehicles()
    return render_template("index.html", vehicles=vehicles)


@app.route("/filter")
def filter():
    searchbar_val = request.args.get("searchbar_val")
    filtered_vehicles = queries.filter_vehicles(searchbar_val)
    return render_template("filter.html", vehicles=filtered_vehicles)


@app.route("/data", methods=["POST"])
def save_data():
    data_file = request.files["data"]
    vehicle_data = json.load(data_file)
    for data_obj in vehicle_data:
        model_year = int(data_obj["model_year"])
        make = data_obj["make"]
        model = data_obj["model"]
        rejection_percentage = float(data_obj["rejection_percentage"].replace(",", "."))
        reason_1 = data_obj["reason_1"]
        reason_2 = data_obj["reason_2"]
        reason_3 = data_obj["reason_3"]
        already_created_vehicle = queries.get_vehicle(model_year, make, model)
        if already_created_vehicle:
            queries.update_vehicle(
                already_created_vehicle.id,
                rejection_percentage,
                reason_1,
                reason_2,
                reason_3,
            )
        else:
            queries.save_vehicle(
                model_year,
                make,
                model,
                rejection_percentage,
                reason_1,
                reason_2,
                reason_3,
            )
    return redirect("/")
