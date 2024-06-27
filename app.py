from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        data = pd.read_excel(filepath)
        fig = px.bar(data, x='Month', y=['Income', 'Expenses'])
        graph = fig.to_html(full_html=False)
        return render_template('graph_Display.html', graph=graph)


if __name__ == '__main__':
    app.run(debug=True)
