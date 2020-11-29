import Transaction
import Wallet
from flask import Flask,jsonify,request,render_template

app=Flask(__name__)
#client can have multiple wallets
client_wallets=[]
#index page
@app.route('/')
def index():
    return render_template('./index.html')

#make_transaction_page
@app.route('/transactions/make')
def make_transactions():
    return render_template('./make_transactions.html')

#view_transactions
@app.route('/transactions/view')
def view_transactions():
    return render_template('./view_transactions.html')

#creating wallet
app.route('/wallet/new',methods=['GET'])
def create_wallet():
    wallet=Wallet()
    response=wallet.to_dict()
    client_wallets.append(wallet)
    return jsonify(response),201

#generating transacion


