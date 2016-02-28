from flask import Flask, url_for, render_template, request
import requests
# import twitter as twit

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


@app.route('/challenge/<merchant_id>', methods='POST')
def new_challenge(merchant_id):
    data = { "merchant_id": merchant_id,
    "_title": request.args.get('photo'),
    "_desc": request.args.get('desc'),
    "_photo": request.files['photo'],
    "_start_date": request.args.get('start'),
    "_end_date": request.args.get('end'),
    "_hashtag": request.args.get('hashtag')}
    insert_into_table("challenges", data)
    twit.post_challenge(merchant_id, data)

@app.route('/coupon/<merchant_id>', methods='POST')
def new_coupon(merchant_id):
    data = { 
        "merchant_id": merchant_id,
        "_title": request.args.get('photo'),
        "_desc": request.args.get('desc'),
        "_photo": request.files['photo'],
        "_start_date": request.args.get('start'),
        "_end_date": request.args.get('end'),
        "_hashtag": request.args.get('hashtag'),
        "_price_usd": request.args.get('price'),
        "_max_number": request.args.get('max_number')
    }
    insert_into_table("coupons", data)
    twit.post_coupon(merchant_id, data)

@app.route('/uber/<user_id>/<merchant_id>/<request_id>', methods='POST')
def request_uber(user_id, merchant_id, request_id):
    data = {
        "user_id": user_id,
        "merchant_id": merchant_id,
        "request_id": request_id,
        "_challenge_id": request.args.get("challenge_id"),
        "_start_lat": request.args.get("start_lat"),
        "_start_lon": request.args.get("start_lon"),
        "_end_lat": request.args.get("end_lat"),
        "_end_lon": request.args.get("end_lon")
    }
    insert_into_table("uber_requests", data)
    notify_merchant(merchant_id, data)
    feed = tunnel_uber(request_id)
    feedback_user(user_id, feed)

if __name__ == '__main__':
    app.run()