import requests
import argparse


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')  # (CBR_API_URL, params=params)
print(response.text)