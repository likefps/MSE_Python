#!/usr/bin/env python
# coding: utf-8

# In[2]:


#240번 문제
def 함수0(num):  # 함수를 정의하는데 함수0은 숫자에 2를 곱한다.
    return num*2
def 함수1(num):  # 함수 1은 (num+2)*2  로 정의된다.
    return 함수0(num+2)
def 함수2(num): #함수2는 ((num+10+2))*2 이다.
    num+=10
    return 함수1(num)
c=함수2(2)  # 그니까 2를 대입하니까.  #28이 출력
print(c)


# In[ ]:




