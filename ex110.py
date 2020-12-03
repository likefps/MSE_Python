#!/usr/bin/env python
# coding: utf-8

# In[1]:


#110 번문제
if True:  #  이미 참 이므로 else는 볼필요가 없음
    if False: # 근데 거짓이니까 else가 실행된다.
        print("1")  
        print("2")
    else:
        print("3")  # 이값이 출련된다.
else:
    print("4")  #여기까지가 첫번쨰 else 문
print("5") # if 문이 끝났으니까  마지막 5가 출력된다.


# In[ ]:




