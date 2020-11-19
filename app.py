from flask import Flask, jsonify, request
from Blockchain import Blockchain
app=Flask(__name__)

blockchain=Blockchain()
@app.route('/transaction/new',methods=['POST'])
def new_Transaction():
    pass

@app.route('/transactions/get')
def get_transactions():
    pass

@app.route('/chain')
def get_chains():
    pass
@app.route('mine')
def mine():
    pass


@app.route('/')
def index():
    pass
# @app.route('/test/req', methods=['POST'])
# def test_req():
#     # pass
#     if request.is_json:
#     # data=request.json
#         data=request.get_json()
#     #     print(data)
#         for key,value in data.items():
#             print(f'key: {key}, value: {value}')
#     return "json confirmed", 200
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5050)