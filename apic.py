from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('index.html')


MERCHANT_DATA = {
    "name": "Chocolate Origin",
    "incoming": [{ "name": "Jack Ong", 
                 "eta": 5,
                 "friend": 2,
                 "img": "jack.png" },
               { "name": "Scott Chue", 
                 "eta": 7,
                 "friend": 3,
                 "img": "scott.png" },
               { "name": "Kang Soon", 
                 "eta": 10,
                 "friend": 3,
                 "img": "kang.png" },
               { "name": "Leo Sjahputra", 
                 "eta": 14,
                 "friend": 4,
                 "img": "leo.png" },
               { "name": "Chua Chin Siang", 
                 "eta": 14,
                 "friend": 1,
                 "img": "ccs.png" }]
}

@app.route('/chocolateorigin')
def console_page():
    return render_template('console.html', data=MERCHANT_DATA)

if __name__ == '__main__':
    app.run()