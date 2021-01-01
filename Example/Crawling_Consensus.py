import requests
from bs4 import BeautifulSoup

def get_bs_obj():
    url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A063080&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701'
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

bs_obj = get_bs_obj()
consensus = bs_obj.find("div",{"class":"bgfbox"})
consensus_score = consensus.find("span")
print(consensus_score.text)