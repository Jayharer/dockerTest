from datetime import datetime
import logging

from . import ExcelFuncs, Convert

class CashEquity:

    def __init__(self, input, date_format):
        self.notional = input['Notional']
        self.underlying = input['UNIQUE_ID']
        self.notionaldate = input['ValuationDate'].date().strftime(date_format)
        self.currency = input['Currency']
        # self.id_type = input['ID_TYPE']
        # self.fxrate = input['fxrate']

    def getModelPriceLocal(self, notional=1, arglast=0.0):
        """ Get Model price of equity """
        result =None
        try:
            notional_date = Convert.ToDateTime(self.notionaldate)
            logging.debug('notional_date : {}'.format(notional_date))
            result = ExcelFuncs.getCashEquityPVFromMktData(
                notional,
                self.underlying,
                notional_date,
                self.currency,
                "",
                arglast
            )
            return round(result, 10)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result



if __name__=="__main__":

    cashequityobj=CashEquity(
        { 'Notional': 100.00
          ,'UNIQUE_ID':"GOOG"
          ,'ValuationDate': "30-10-2020"
          ,'Currency': "USD"
        }
    )
    print(cashequityobj.getModelPriceLocal(cashequityobj.notional))
