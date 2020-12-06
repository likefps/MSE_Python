#!/usr/bin/env python
# coding: utf-8

# In[2]:


#220번 문제
def print_max(a,b,c):  # 함수를 선언하면서 임의의 숫자 3개를 놓는다.
    if a>b and a>c:  # 가정을하는데 만약 a 가 가장크다는 if문으로 나타낸다.
        print(a) # a 가 가장 크니까 a 출력 
    elif b>a and b>c:# a가 가장크지 않고 (elif) b가 가장크다고 가정하면
        print(b) #b출력
    else:
        print(c)  #  위에게 아니면 c가 가장 최대일테니 c 출력
print_max(5,3,1) #숫자를 넣어서 해보면 최대값이 출력된다. 함수 완성
        


# In[ ]:




