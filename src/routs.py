from src import app
from flask import request
from src import pricer
from datetime import datetime
from flask import jsonify
import logging
from . import Convert

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route('/cashequity/modelpricelocal', methods=['GET','POST'])
def handle_cashequity():
    if request.method == 'GET':
        if request.is_json:
            data = request.get_json()
            date_format = data['date_format']
            logging.debug('date_format: {}'.format(date_format))
            logging.debug('date : {}'.format( data['ValuationDate']))
            data['ValuationDate'] = datetime.strptime(data['ValuationDate'],date_format)
            cash_equity = pricer.CashEquity(data, date_format)
            model_price = cash_equity.getModelPriceLocal(cash_equity.notional)
            logging.debug('model price: {}'.format(model_price))
            return jsonify({"model_price": str(model_price)})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/datetime', methods=['GET','POST'])
def handle_datetime():
    if request.method == 'GET':
        if request.is_json:
            data = request.get_json()
            try:
               result = Convert.ToDateTime(data['ValuationDate'])
               logging.debug('ValuationDate : {} '.format(result))
               return jsonify({"date": str(result) })
            except Exception as e:
                return jsonify({"error": "error"})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})