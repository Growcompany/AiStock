import requests
from bs4 import BeautifulSoup


url = 'http://comp.fnguide.com/SVO2/ASP/SVD_ProResultCorp.asp?pGB=1&gicode=A003490&cID=&MenuYn=Y&ReportGB=&NewMenuID=503&stkGb=701' #이 주소안에 테스트할 url넣기만하면됨
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

print(bs_obj)