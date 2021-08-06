from src import app
from flask import request
from src import pricer
from datetime import datetime

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route('/cashequity/modelpricelocal', methods=['GET'])
def handle_cashequity():
    if request.method == 'GET':
        if request.is_json:
            data = request.get_json()
            data['ValuationDate'] = datetime.strptime(data['ValuationDate'],'%d-%m-%Y')
            cash_equity = pricer.CashEquity(data)
            model_price = cash_equity.getModelPriceLocal(cash_equity.notional)
            return {"model_price": model_price}
        else:
            return {"error": "The request payload is not in JSON format"}