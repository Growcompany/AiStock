import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time

#함수 1.원하는 재무테이블 가져오기
def fs_data(code):
    url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701&gicode=A' + code
    res = requests.get(url)
    df = pd.read_html(res.text)
    temp_df=df[0]
    temp_df=temp_df.set_index(temp_df.columns[0])
    temp_df=temp_df[temp_df.columns[:4]]
    temp_df=temp_df.loc[['매출액','영업이익','당기순이익']]
    return temp_df

#함수 2.행열변환 및 테이블 수정
def change_df(code,fs_df):
    for num,col in enumerate(fs_df.columns):
        temp_df=pd.DataFrame({code:fs_df[col]})
        temp_df=temp_df.T
        temp_df.columns=[[col]*len(fs_df),temp_df.columns]
        if num ==0:
            total_df=temp_df
        else:
            total_df=pd.merge(total_df,temp_df,how='outer',left_index=True,right_index=True)        
    return total_df

#본문코드
code = ['005930','000660', '207940', '035420', '068270']
for num, code in enumerate(code):
    fs_data_frame=fs_data(code)
    fs_data_frame_changed=change_df(code,fs_data_frame)
    if num ==0:
        total_fs = fs_data_frame_changed
    else:
        total_fs=pd.concat([total_fs,fs_data_frame_changed])
print(total_fs)