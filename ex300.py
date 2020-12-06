#!/usr/bin/env python
# coding: utf-8

# In[1]:


#300번문제
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))  # 10.31은 잘 변환되고--> clean data ---> 변환완료
    except:
        print(0) # "" 에 대해서 0으로 출력됨 --> 예외가 발생했으니가 clean data 는 안뜸       변환완료는 상관 없응니까 출력됨
    else:
        print("clean data")   # 8은 정상적으로 변환되니까 cleandata 변환완료 출력
    finally:
        print("변환 완료")


# In[ ]:




