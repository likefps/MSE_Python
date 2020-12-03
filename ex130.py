#!/usr/bin/env python
# coding: utf-8

# In[4]:


#130번 문제
import requests # 원하는 사이트의 html 주소의 내용을 가져와 주는 역활
btc=requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc에 시가, 종가, 최저 최고값이 저장된다. 

변동폭=float(btc['max_price'])-float(btc['min_price']) 
#실수형 자료형이므로 float을 사용하며 변동폭 이므로 최고값에서 최저값을 뺴준것을 저장한다.

시가=float(btc['opening_price']) # 시작가격 을 저장해준다.
최고가=float(btc['max_price'])  # 최고가격을 저장해준다.
최저가=float(btc['min_price'])  # 최저가격을 저장해준다.

if(시가+변동폭)>최고가: #문제에서 나온 정의대로 조건문을 완성시킨다.
    print("상승장")
else:
    print("하락장")


# In[ ]:




