#!/usr/bin/env python
# coding: utf-8

# In[6]:


#170번 문제
a=list(range(1,11,1))
s=1  # s=1로 선언해줘야하는 이유는 곱셈의 항등원이 1이기 때문이다. 
for i in a: # 리스트에 대해 조건문을 돌리는데
    s=s*i # s =1 *1 이 다시 s 로 들어가고 1*2 가 다시 s 로 들어가고 그러면 (1*2)*3이 s 에 들어가고 착착 진행하면 (1*2*3*....*10)까지 계산하게된다.
s


# In[ ]:




