from datetime import datetime, date
import logging

from src import ExcelFuncs, Convert
from src import utilspy

class CashEquity:

    def __init__(self, input):
        self.notional = input['Notional']
        self.underlying = input['UNIQUE_ID']
        self.notionaldate = input['ValuationDate']
        self.currency = input['Currency']
        # self.id_type = input['ID_TYPE']
        # self.fxrate = input['fxrate']

    def getModelPriceLocal(self, notional=1, arglast=0.0):
        """ Get Model price of equity """
        result =None
        try:
            result = ExcelFuncs.getCashEquityPVFromMktData(
                notional,
                self.underlying,
                self.notionaldate,
                self.currency,
                "",
                arglast
            )
            return round(result, 10)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

class EquityOption:

    def __init__(self, input):
        self.equityname = input['EquityName']
        self.strike = input['Strike']
        self.optiontype = input['OptionType']
        self.maturity = utilspy.convert_date_to_excel_number(input['Maturity'].date())
        self.valuationdate = utilspy.convert_date_to_excel_number(input['ValuationDate'].date())

    def getModelPriceLocal(self):
        result = None
        try:
            result = ExcelFuncs.GetEquityOptionPriceFromMarketData(
                self.equityname
                , self.strike
                , self.optiontype
                , self.maturity
                , self.valuationdate
            )
            return round(result, 10)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

    def getDelta(self):
        result = None
        try:
            result = ExcelFuncs.GetEquityOptionDeltaFromMarketData(
                self.equityname
                , self.strike
                , self.optiontype
                , self.maturity
                , self.valuationdate
                , 0.01
            )
            return round(result, 10)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

    def getVega(self):
        result = None
        try:
            result = ExcelFuncs.GetEquityOptionVegaFromMarketData(
                self.equityname
                , self.strike
                , self.optiontype
                , self.maturity
                , self.valuationdate
                , 0.0001
            )
            return round(result, 10)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

class Bond:

    def __init__(self, input):
        self.valuationdate = utilspy.convert_date_to_excel_number(input['ValuationDate'].date())
        self.isin = input['UNIQUE_ID']
        self.notional = input['Notional']

    def getModelPriceLocal(self):
        result = None
        try:
            result = ExcelFuncs.GetBondPVFromMarketData(
                self.valuationdate,
                self.isin,
                self.notional)
            return round(result / self.notional, 4)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

    def getDV01(self):
        result = None
        try:
            result = ExcelFuncs.GetBondIRDeltaFromMarketData(
                self.valuationdate,
                self.isin,
                self.notional)
            return round(result, 6)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

class FXOptionEuropean:

    def __init__(self, input):
        self.valuationdate = Convert.ToDateTime(
            input['ValuationDate'].strftime('%d-%m-%Y'))
        self.optiontype = input['OptionType']
        self.underlying = input['CurrencyPair']
        self.strike = input['Strike']
        self.expiry = Convert.ToDateTime(
            input['Maturity'].strftime('%d-%m-%Y'))
        self.notional = input['Notional']

    def getModelPriceLocal(self):
        result = None
        try:
            result = ExcelFuncs.getFXOptionPriceFromMktData(
                self.valuationdate
                , self.optiontype
                , self.underlying
                , self.strike
                , self.expiry
                , self.notional
            )
            return round(result, 4)
        except Exception as e:
            logging.error(e, exc_info=True)
            return result

if __name__=="__main__":

    # cashequityobj=CashEquity(
    #     { 'Notional': 100.00
    #       ,'UNIQUE_ID':"GOOG"
    #       ,'ValuationDate': "30-10-2020"
    #       ,'Currency': "USD"
    #     }
    # )
    # print(cashequityobj.getModelPriceLocal(cashequityobj.notional))

    # eqoption1 = EquityOption({
    #     "EquityName": 'APOLLOHOSP'
    #     , "Strike": 2400
    #     , "OptionType": "CALL"
    #     , "Maturity": datetime(2020,11,26)
    #     , "ValuationDate": datetime(2020, 10, 30)
    #     , "Notional": 1
    #     , "Currency": 'INR'
    # })
    # print(eqoption1.getModelPriceLocal())

    # bondobj = Bond({"ValuationDate": datetime(2020,2,14),
    #                                 "UNIQUE_ID": "67066GAE4",
    #                                 "Notional": 1,})
    # print(bondobj.getModelPriceLocal())

    fxoption1=FXOptionEuropean({
    "ValuationDate":date(2019,3, 12)
    ,"OptionType":"Put"
    ,"CurrencyPair": 'EURUSD'
    ,"Strike":1.120
    ,"Maturity":date(2019,4,15)
    ,"Notional":100000.00
    })
    print(fxoption1.getModelPriceLocal())
