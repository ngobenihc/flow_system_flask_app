from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        file = request.files['file']

        # Save the file to a temporary location
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process the file and generate a graph
        data = pd.read_excel(file_path)
        plt.figure()
        data.plot(x='Month', y=['Income', 'Expenses'], kind='bar')
        graph_path = os.path.join(STATIC_FOLDER, 'graph.png')
        plt.savefig(graph_path)

        return redirect(url_for('show_graph'))


@app.route('/graph')
def show_graph():
    # Displaying the graph
    return '<img src="/static/graph.png" alt="Graph">'


if __name__ == '__main__':
    app.run(debug=True)
