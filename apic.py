from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('index.html')


MERCHANT_DATA = {
    "name": "Chocolate Origin",
    "incoming": [{ "name": "Jack Ong", 
                 "eta": "5mins" },
               { "name": "Scott Chue", 
                 "eta": "7mins" },
               { "name": "Kang Soon", 
                 "eta": "10mins" },
               { "name": "Leo Sjahputra", 
                 "eta": "14mins" },
               { "name": "Chua Chin Siang", 
                 "eta": "14mins" }]
}

@app.route('/chocolateorigin')
def console_page():
    return render_template('console.html', data=MERCHANT_DATA)

if __name__ == '__main__':
    app.run()