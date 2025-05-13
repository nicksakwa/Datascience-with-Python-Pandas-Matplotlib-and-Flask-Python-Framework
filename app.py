from flask import Flask, send_file
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os

app= Flask(__name__)

@app.route('/plot.png')
def plot_png():
    try:
        health_data=pd.read_csv("data.csv", header=0, sep=",")
    except FileNotFoundError:
        plt.figure(figsize=(6,4))
        plt.text(0.5,0.5, "Data file not found!", ha='center', va='center')
        plot_filename ='error.png'
        plt.savefig(plot_filename)
        return send_file(plot_filename, mimetype='image/png')
    
    plt.figure()
    health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)

    plot_filename='plot.png'
    plt.savefig(plot_filename)

    return send_file(plot_filename, mimetype='image/png')
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health data plot</title>
    </head>
    <body>
        <h1> Health Data Visualization</h1>
        <img src="/plot.png" alt="Health Data Plot">
    <body>
    </html>
    """
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
