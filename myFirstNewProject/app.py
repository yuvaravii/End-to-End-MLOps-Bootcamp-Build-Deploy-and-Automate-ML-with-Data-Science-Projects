# Objective: To create the flask --> a light weight Web server gateway interface

from flask import Flask, render_template, request
import os
import numpy as np
from src.my_first_end_to_end_project.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulphur_dioxide = float(request.form['free_sulphur_dioxide'])
            total_sulphur_dioxide = float(request.form['total_sulphur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulphur_dioxide,
                total_sulphur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]

            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            prediction = obj.predict(data)

            return render_template('results.html', prediction=str(prediction))

        except Exception as e:
            return str(e)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
