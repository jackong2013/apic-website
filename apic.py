from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('index.html')


@app.route('/<merchant>')
def console_page(merchant):
    return render_template('console.html', merchant=merchant)

if __name__ == '__main__':
    app.run()