#!/usr/bin/env python
# coding: utf-8

# In[1]:


#290번 문제
class 부모:  # 부모 클래스 정의
  def __init__(self): #생성자
    print("부모생성")

class 자식(부모): #자식칼래스는 부모클래스를 상속받음
  def __init__(self): 
    print("자식생성") # 자식생성을 출력..
    super().__init__() # 부모클래스에 접근해서 호출.. self는 알아서 전달이된다.

나 = 자식() # 자식클래스 에 객체를 생성     # 먼저 자식생성클래스를 생성 부모클래스를 명시적으로 호출했기때문데  super() 부모생성이 출력됨


# In[ ]:




