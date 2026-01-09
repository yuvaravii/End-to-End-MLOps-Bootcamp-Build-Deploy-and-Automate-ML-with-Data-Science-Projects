# Objective: To create the flask --> a light weight Web server gateway interface , used for faster and Lighter application.

from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.my_first_end_to_end_project.pipeline.prediction_pipeline import PredictionPipeline


app = Flask(__name__)

@app.route('/', methods= ['GET']) ## This will create the home page
def homepage():
    return render_template("index.html")

 