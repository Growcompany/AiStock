import requests
from bs4 import BeautifulSoup


url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A063080&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701' #이 주소안에 테스트할 url넣기만하면됨
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

print(bs_obj)