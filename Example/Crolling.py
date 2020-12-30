import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time

code = ['A005930', 'A063080', 'A044480']

def f_data(code):
    url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701&gicode'+code
    res = requests.get(url)
    df = pd.read_html(res.text)
    print(code)
    return df[0]

for code in code:
    dataframe=f_data(code)
    dataframe=dataframe.set_index(dataframe.columns[0])
    dataframe=dataframe[dataframe.columns[:4]]
    dataframe=dataframe.loc[['매출액','영업이익','당기순이익']]
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))

