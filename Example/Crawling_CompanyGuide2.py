import requests
from bs4 import BeautifulSoup as bs

#삭제할 키값들
DelKey = ['ISSUE' , 'GS_GB', 'REP_GB', 'SALES', 'REVERT', 'REVERT2', 'DA_GB', 'DIS_DT']

#전년동기대비 매출액 퍼센트 "SALES2" 전년동기대비 영업이익 "OPER2" 전년동기대비 순이익 "NET2" 분기실적 영업이익 "OPER" 분기실적 순이익 "NET"

url = 'http://comp.fnguide.com/SVO2/common/sp_read_json_cache.asp?cmdText=menu_9_1&IN_gs_ym=202010&IN_gs_gb=N&IN_report_gb=X&IN_gb=D&IN_SRC_GB=SVO&_=1609502494130'
response = requests.get(url)
jsonObjs = response.json()
dataList = jsonObjs['data'] 

for data in dataList :
    for Key in DelKey:
        del data[Key]
    print(data)
    if data['ITEMNM'] == '빅히트':
        print(data)
        break