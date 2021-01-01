import requests
import re
from bs4 import BeautifulSoup

def search_news():
    url = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&date=20201231&page=1'
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    tags = bs_obj.find_all('dd',{"class":"articleSummary"})

    for tag in tags:
        try:
            companycode = tag.text
            companycode = companycode[companycode.index("(")+1:]
            companycode = companycode[:companycode.index(")")]
            numbers = re.findall("\d+", companycode)
            if len(numbers[0])==6:
                print(numbers[0])
        except:
            pass
        
search_news()
