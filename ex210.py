#!/usr/bin/env python
# coding: utf-8

# In[1]:


#210번문제
def message1():  # def는 함수를 정의할떄 쓴다. message1은 A가 출력되고, 2는 B 가 출력된다.
    print('A')
def message2():
    print('B')
    
def message3():   # message3은 for문을 돌려서 정의하는데
    for i in range(3): # 0부터 2까지 총 3번 반복하는데
        message2()  # 2는 B를 정의한다고 했고
        print('C')  #  C는 그냥 출력하는거고   이 두문장을 3번 반복한뒤에
    message1()  # message1인 A를 출력하면 된다.
message3()


# In[ ]:




