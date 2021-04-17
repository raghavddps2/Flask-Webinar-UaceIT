# Importing the Flask Class - Instance of this class will be our WSGI application.
# Web Server Gateway Interface

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

'''
The line below will create an instance of the Flask class - The First argument is the
name of the application's module or package.
'''
app = Flask(__name__)


cred = credentials.Certificate('key.json')
initialize_app(cred)

db = firestore.client()
crypto_ref = db.collection('cryptos')

'''
We then use the route decorator to tell Flask what URL should trigger our function.
We use the route decorator to bind a function to a URL.
'''

@app.route('/add',methods=["POST"])
def create():

    try:
        symbol = request.json["symbol"]
        crypto_ref.document(symbol).set(request.json)
        return jsonify({"Success":True}), 200

    except Exception as e:
        return jsonify({"Message":"An Error Occured"}), 500


@app.route('/get',methods=["GET"])
def get():

    try:

        crypto_symbol = request.args.get("symbol")
        if crypto_symbol:
            crypto = crypto_ref.document(crypto_symbol).get()
            return jsonify(crypto.to_dict()), 200
        else:
            cryptos = [crypto.to_dict() for crypto in crypto_ref.stream()]
            return jsonify(cryptos), 200

    except Exception as e:
        return jsonify({"Message":"An Error Occured"}), 500
    
@app.route('/update',methods=["PUT"])
def update():
    
    try:
        symbol = request.json["symbol"]
        crypto_ref.document(symbol).update(request.json)
        return jsonify({"Success":True}), 200

    except Exception as e :
        return jsonify({"Message":"An Error Occured"}), 500

@app.route('/delete',methods=["DELETE"])
def delete():

    try:
        crypto_symbol = request.args.get("symbol")
        crypto_ref.document(crypto_symbol).delete()
        return jsonify({"Success":True}), 200

    except Exception as e:
        print(e)    
        return jsonify({"Message":"Error Occured"}), 500
        

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)