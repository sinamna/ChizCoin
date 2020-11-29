import Transaction
import Wallet
from flask import Flask,jsonify,request,render_template

app=Flask(__name__)
#index page
@app.route('/')
def index():
    return render_template('./index.html')

#make_transaction_page
@app.route('/make/transactions')
def make_transactions():
    return render_template('./make_transactions.html')

#view_transactions

#creating wallet

#generating transacion


