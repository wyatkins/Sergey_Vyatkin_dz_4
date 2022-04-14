""" my module """

# import decimal
from datetime import datetime

import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    """ we get the current rate by currency code from the site """

    if not (currency_code and url):
        return None

    # fix register
    currency_code = currency_code.upper()

    # take respond from url
    respond = requests.get(url)

    if respond.ok:

        text = respond.text

        cur = text.split(currency_code)

        # if no found currency
        if len(cur) == 1:
            return None

        # take value param from text
        value = cur[1].split("</Value>")[0].split("<Value>")[1]

        # conver to float
        value = float(value.replace(",", "."))

        # conver to decimal
        #decimal.getcontext().prec = 4
        #value = decimal.Decimal(value.replace(",", "."))

        # parse date from respond
        date = respond.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()

        return (value, date)

    else:
        return None