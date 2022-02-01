#!python3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model=joblib.load("lin_model")

@app.route('/', methods=['GET', 'POST'])
def index():
    calorie = ''
    if request.method == 'POST':
        weight = float(request.form.get('Weight'))
        height = float(request.form.get('Height'))
        age    = float(request.form.get('Age'))
        gender = request.form.get('Gender')
        activity = request.form.get('Activity')
        intensity = request.form.get('Intensity')
        duration = float(request.form.get('Duration'))
        if gender == "Female":
            gender = 0
        else:
            gender = 1
        if activity == "Outdoor Games":
            activity=0
        elif activity == "Running":
            activity =1
        elif activity == "Walking":
            activity =2
        elif activity == "cardi-gym-activities":
            activity =3
        elif activity == "Cycling":
            activity =4
        elif activity == "Swimming":
            activity =5
        else:
            activity=6
        if intensity =="Light":
            intensity = 0
        elif intensity == "Moderate":
            intensity =1
        else:
            intensity = 2
        calorie =model.predict([[gender,age,height,weight,activity,intensity,duration]]) 
    return render_template("calorie_calc.html",
	                        calorie=calorie)

if __name__ == '__main__':
    app.run()                                 