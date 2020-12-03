#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 160번 문제
list=['intra.h','intra.c','define.h','run.py']
for i in list:
    name,ext=i.split(".") # 파일 이름과(name), 확장자(ext)를 "."을 기준으로 분리한다.
    if(ext=='h') or (ext=='c'): # 여기서 분리된 확장자가 h 이거나 c이면 
        print(i) # name 과 확장자가 동시에 담겨있는 변수 i를 출력한다.


# In[ ]:





# In[ ]:





# In[ ]:




