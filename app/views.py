from app import app
from app.transactions import Transaction
from flask import request,jsonify

trans = Transaction() #ONE ISTANCE NEEDED HERE BECAUSE EVERY SERIES OF TRANSACTIONS IS UNIQUE

@app.route("/transactions",methods=["POST"])
def post_transactions():
    global trans #GLOBAL KEYWORD USED TO UNDERLINE I'M USING THE RIGHT REFERENCE, INSTEAD OF RUNNING ANOTHER ONE NEWER
    trans.transaction.append(request.json) #ADD MORE AND MORE TRANSACTIONS
    
    if trans.check_time(request.json.get("timestamp")):
        return "201"
    else:
        return "204"

@app.route("/statistics",methods=["GET"])
def get_statistics():
    global trans
    return jsonify(trans.get_transactions(trans.transaction))
    