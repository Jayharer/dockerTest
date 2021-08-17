from datetime import date,datetime
import traceback
from pathlib import Path


def convert_date_to_excel_number(datevalue):
    """ Convert datetime value into numeric value

    :param datevalue: python datetime value.
    :type datevalue: date.
    :returns: int -- Number equivalent to datetime.

    >>> convert_date_to_excel_number(date(2019,2,21))
    43517
    """
    offset = 693594
    current = date(datevalue.year, datevalue.month, datevalue.day)
    n = current.toordinal()
    return (n - offset)

def xlnumdate_to_datetime(xldate):
    """ Convert date numeric value into python datetime

    :param xldate: numeric value of date.
    :type xldate: int.
    :returns: datetime --  Datetime equivalent to given xldate.

    >>> xlnumdate_to_datetime(43517)
    2019-02-21 00:00:00
    """
    dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + xldate - 2)
    return datetime(dt.year,dt.month,dt.day)
