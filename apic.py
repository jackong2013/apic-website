from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()