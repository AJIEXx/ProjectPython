# Младший брат тг-бота @anything_notslava_bot, который сможет перевести рубли в драхмы за 5 секунд.
#
# В коде слишком длинный список, так что фулл код по ссылке --> (тык)

import requests
import json
import sys
from pprint import pprint

# The below 4 lines bring out the value of currency from the api at fixer.io.  I had to register there, the key is unique to me.
url = "http://data.fixer.io/api/latest?access_key=33ec7c73f8a4eb6b9b5b5f95118b2275"
data = requests.get(url).text
data2 = json.loads(data)  # brings whether request was successful,timestamp etc
fx = data2["rates"]

currencies = [
    "AED : Emirati Dirham,United Arab Emirates Dirham",

    ............

    "ZWL : Zimbabwean Dollar,Zimbabwe Dollar",
]


# The below function calculates the actual conversion
def function1():
    query = input(
        "Please specify the amount of currency to convert, from currency, to currency (with space in between).\nPress SHOW to see list of currencies available. \nPress Q to quit. \n"
    )
    if query == "Q":
        sys.exit()
    elif query == "SHOW":
        pprint(currencies)
        function1()
    else:
        qty, fromC, toC = query.split(" ")
        fromC = fromC.upper()
        toC = toC.upper()
        qty = float(round(int(qty), 2))
        amount = round(qty * fx[toC] / fx[fromC], 2)
        print(f"{qty} of currency {fromC} amounts to {amount} of currency {toC} today")


try:
    function1()
except KeyError:
    print("You seem to have inputted wrongly, retry!")
    function1()