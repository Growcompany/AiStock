import pandas as pd

def make_code(x):
    x=str(x)
    return 'A'+ '0'*(6-len(x)) + x


code_data = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
code_data = code_data[['종목코드','회사명']]
code_data['종목코드'] = code_data['종목코드'].apply(make_code)
print(code_data)