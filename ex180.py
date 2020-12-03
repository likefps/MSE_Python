#!/usr/bin/env python
# coding: utf-8

# In[7]:


#180번문제
low_prices =[100,200,400,800,1000]
high_prices=[150,300,430,880,1000]
volatility=[] # 변동폭을 빈 리스트로 만들어 넣고.
for i in range(len(low_prices)): # 저가 리스트 길이 5번만큼 반복하는데
        volatility.append(high_prices[i]-low_prices[i]) # 아까 만들어놨던 빈 변동폭 리스트에 다음값을 추가해서(append)(뒤에 붙여넣는거) 넣어준다.
volatility


# In[ ]:




