from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    print url_for('static', filename='style.css')
    return render_template('index.html')
