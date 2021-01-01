import io
import json
import sys
import urllib.request as req

from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
ua = UserAgent()

# 헤더 선언
headers = {
    'User-Agent': ua.ie,
    'referer': 'http://finance.daum.net/domestic/volume'
}

#불러올 페이지 숫자
page_number = 3

url = []
res = []
rank_json = []
# 다음 주식 요청 URL
for i in range(0,page_number+1):
# print(request.get_method())   #Post or Get 확인
# print(request.get_full_url()) #요청 Full Url 확인
    url.append('http://finance.daum.net/api/trend/trade_volume?page='+str(i+1)+'&perPage=30&fieldName=accTradeVolume&order=desc&market=KOSPI&pagination=true')
# 요청
    res.append(req.urlopen(req.Request(url[i], headers=headers)).read().decode('utf-8'))
# 응답 데이터 확인(Json Data)
# print('res', res)
# 응답 데이터 str -> json 변환 및 data 값 저장
    rank_json.append(json.loads(res[i])['data'])
# 중간 확인
#print('중간 확인 : ', rank_json, '\n')
    for elm in rank_json[i]:
        # print(type(elm)) #Type 확인
        print('순위 : {}, 회사명 : {}'.format(elm['rank'], elm['name']), )
