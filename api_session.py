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
        if symbol in session.keys():
            return jsonify({"Message":"Symbol Already Exists"}), 200
        session[symbol] = request.json
        return jsonify({"Success":True}), 200

    except Exception as e:
        return jsonify({"Message":"An Error Occured"}), 500


@app.route('/get',methods=["GET"])
def get():

    try:
        crypto_symbol = request.args.get("symbol")
        if crypto_symbol:
            if crypto_symbol not in session.keys():
                return jsonify({"Message":"Symbol Does not exist"}), 200
            crypto = session[crypto_symbol]
            return jsonify(crypto), 200
        else:
            result = [value for value in session.values()]
            return jsonify(result), 200

    except Exception as e:
        return jsonify({"Message":"An Error Occured"}), 500
    
@app.route('/update',methods=["PUT"])
def update():
    
    try:
        symbol = request.json["symbol"]
        if symbol in session.keys():    
            session[symbol] = request.json
            return jsonify({"Success":True}), 200
        else:
            return jsonify({"Success":"Symbol does not exist"}), 400

    except Exception as e :
        return jsonify({"Message":"An Error Occured"}), 500
    
    

@app.route('/delete',methods=["DELETE"])
def delete():

    try:
        symbol = request.args.get("symbol")
        if symbol in session.keys():    
            session.pop(symbol)
            return jsonify({"Success":True}), 200
        else:
            return jsonify({"Success":"Symbol does not exist"}), 400

    except Exception as e: 
        return jsonify({"Message":"Error Occured"}), 500
        

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)