# Importing the Flask Class - Instance of this class will be our WSGI application.
# Web Server Gateway Interface

from flask import Flask, request, jsonify, session

'''
The line below will create an instance of the Flask class - The First argument is the
name of the application's module or package.
'''
app = Flask(__name__)

app.secret_key = "secret@123"

'''
We then use the route decorator to tell Flask what URL should trigger our function.
We use the route decorator to bind a function to a URL.
'''

@app.route('/add',methods=["POST"])
def create():

    try:
        symbol = request.json["symbol"]
        session[symbol] = request.json
        return jsonify({"Success":True}), 200

    except Exception as e:
        return jsonify({"Message":"An Error Occured"}), 500


@app.route('/get',methods=["GET"])
def get():

    try:
        crypto_symbol = request.args.get("symbol")
        if crypto_symbol:
            crypto = session[crypto_symbol]
            return jsonify(crypto), 200
        else:
            cryptos = [value for value in session.values()]
            return jsonify(cryptos), 200

    except Exception as e:
        print(e)
        return jsonify({"Message":"An Error Occured"}), 500
    
@app.route('/update',methods=["PUT"])
def update():
    
    try:
        symbol = request.json["symbol"]
        session[symbol] = request.json
        return jsonify({"Success":True}), 200

    except Exception as e :
        return jsonify({"Message":"An Error Occured"}), 500

@app.route('/delete',methods=["DELETE"])
def delete():

    try:
        crypto_symbol = request.args.get("symbol")
        session.pop(crypto_symbol)
        return jsonify({"Success":True}), 200

    except Exception as e:
        print(e)    
        return jsonify({"Message":"Error Occured"}), 500
        

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)