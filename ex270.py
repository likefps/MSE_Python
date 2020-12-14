#!/usr/bin/env python
# coding: utf-8

# In[17]:


#270문제
class Stock: # stock 클래스 
    def __init__(self, name, code, per, pbr, 배당수익률):   # 호출 
        self.name = name # 선언
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

   

종목 = []  # 종목에 담을 빈리스트 생성하고 

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)  # 자료 입력 
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)   # 리스트로 자료를 추가해줌
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)  #  i 가 stock 객체를 엮어준다. 그러니까 삼성 --> lg 전자 순으로 코드와 per 값이 출력된다.


# In[ ]:




