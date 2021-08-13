import clr, sys, os
import config
from datetime import datetime

from src import ExcelFuncs, Convert


class CashEquity:

    def __init__(self, input):
        self.notional = input['Notional']
        self.underlying = input['UNIQUE_ID']
        self.notionaldate = input['ValuationDate'].date().strftime('%d-%m-%Y')
        self.currency = input['Currency']
        # self.id_type = input['ID_TYPE']
        # self.fxrate = input['fxrate']

    def getModelPriceLocal(self, notional=1, arglast=0.0):
        """ Get Model price of equity by ExcelFuncs.getCashEquityPVFromMktData() """
        try:
            result = ExcelFuncs.getCashEquityPVFromMktData(
                notional,
                self.underlying,
                Convert.ToDateTime(self.notionaldate),
                self.currency,
                "",
                arglast
            )
            return round(result, 10)
        except Exception as e:
            return e



if __name__=="__main__":

    cashequityobj=CashEquity(
        { 'Notional': 100.00
          ,'UNIQUE_ID':"GOOG"
          ,'ValuationDate': datetime(2020,10,30)
          ,'Currency': "USD"
        }
    )
    print(cashequityobj.getModelPriceLocal(cashequityobj.notional))
