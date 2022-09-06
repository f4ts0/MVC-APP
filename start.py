## ovo je kontroller
from crypt import methods
from importlib.resources import path
from flask import Flask, app, render_template, request
from database import Database

#crate flask obj and initiate database object
app = Flask(__name__)
#path = "/Users/istankov/Downloads/polumenta-master/OOP/devnet sa plurala/MVC APP/data/db.json"
path = "/Users/istankov/Downloads/polumenta-master/OOP/devnet sa plurala/MVC APP/data/db.yml"
db = Database(path)


@app.route("/", methods=["GET", "POST"])
def index():
    print(dir(request))  
    
    if request.method == "POST":
        acct_id = request.form["acct_id"]
        print(acct_id)
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"balance for {acct_id}: {acct_balance}")
    else:
        acct_balance = "nema acc"
        acct_id = "nema"
    
    igor_test="jajajaja"

    return render_template("index.html", acct_balance=acct_balance, acct_id=acct_id, igor_test=igor_test)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
        