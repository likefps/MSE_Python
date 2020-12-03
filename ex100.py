#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 100번문제
data=['09/05','09/07','09/08','09/09']
close_price=[10500,10300,10100,10800,11000]
close_table=dict(zip(data,close_price)) # zip 은 여러 리스트에 담긴 여러 값으로 새로운 리스트로 만들떄 사용하는데 이걸 딕셔너리로 만드려고 하니까 dict(zip()) 해서 변수에 담아준다.
print(close_table)


# In[ ]:




