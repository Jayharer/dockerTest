from src import app
from flask import request
from src import pricer
from datetime import datetime
from flask import jsonify
import logging
from src import Convert

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route('/cashequity/modelpricelocal', methods=['GET','POST'])
def handle_cashequity():
    if request.method == 'GET':
        if request.is_json:
            data = request.get_json()
            logging.debug('date : {}'.format( data['ValuationDate']))
            cash_equity = pricer.CashEquity(data)
            model_price = cash_equity.getModelPriceLocal(cash_equity.notional)
            logging.debug('cashequity model price: {}'.format(model_price))
            return jsonify({"model_price": str(model_price)})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/equityoption/modelprice', methods=['GET','POST'])
def handle_equityoption():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        data['Maturity'] = datetime.strptime(data['Maturity'], '%d-%m-%Y')
        eq_option = pricer.EquityOption(data)
        model_price = eq_option.getModelPriceLocal()
        logging.debug('eq_option model price: {}'.format(model_price))
        return jsonify({"model_price": str(model_price)})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/equityoption/delta', methods=['GET','POST'])
def handle_equityoption_delta():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        data['Maturity'] = datetime.strptime(data['Maturity'], '%d-%m-%Y')
        eq_option = pricer.EquityOption(data)
        model_price = eq_option.getDelta()
        logging.debug('eq_option delta : {}'.format(model_price))
        return jsonify({"eq_option delta": str(model_price)})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/equityoption/vega', methods=['GET','POST'])
def handle_equityoption_vega():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        data['Maturity'] = datetime.strptime(data['Maturity'], '%d-%m-%Y')
        eq_option = pricer.EquityOption(data)
        model_price = eq_option.getVega()
        logging.debug('eq_option vega : {}'.format(model_price))
        return jsonify({"eq_option vega": str(model_price)})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/bond/modelprice', methods=['GET','POST'])
def handle_bond():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        eq_option = pricer.Bond(data)
        model_price = eq_option.getModelPriceLocal()
        logging.debug('bond price : {}'.format(model_price))
        return jsonify({"bond price": str(model_price)})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/bond/irdelta', methods=['GET','POST'])
def handle_bond_irdelta():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        eq_option = pricer.Bond(data)
        model_price = eq_option.getDV01()
        logging.debug('bond irdelta : {}'.format(model_price))
        return jsonify({"bond irdelta": str(model_price)})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})

@app.route('/fxoption/price', methods=['GET','POST'])
def handle_fx_price():
    if request.is_json:
        data = request.get_json()
        logging.debug('date : {}'.format( data['ValuationDate']))
        data['ValuationDate'] = datetime.strptime(data['ValuationDate'], '%d-%m-%Y')
        data['Maturity'] = datetime.strptime(data['Maturity'], '%d-%m-%Y')
        eq_option = pricer.FXOptionEuropean(data)
        model_price = eq_option.getModelPriceLocal()
        logging.debug('fx_price : {}'.format(model_price))
        return jsonify({"fx_price ": str(model_price)})
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
                logging.error(e, exc_info=True)
                return jsonify({"error": "error"})
        else:
            return jsonify({"error": "The request payload is not in JSON format"})