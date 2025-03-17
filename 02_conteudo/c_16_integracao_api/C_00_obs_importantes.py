# Não é necessário intalar a StringIO, vem com o Python.
from io import StringIO
import pandas as pd
import requests

from chave import chave_api

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=ITUB4.SAO&apikey={chave_api}&datatype=csv'
r = requests.get(url)

# io converte um determinado texto em um ARQUIVO temporário
# read_csv(precisa de um arquivo como parâmetro)
tabela = pd.read_csv(StringIO(r.text))