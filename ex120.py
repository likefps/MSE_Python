#!/usr/bin/env python
# coding: utf-8

# In[2]:


#120번 문제
fruit={"봄":"딸기",'여름':'토마토','가을':'사과'}
que=input("좋아하는 과일은?")  # 사용자로부터 입력을 받는다. c언어 scanf같은거
if que in fruit.values(): #fruit.values 는 fruit 안에 벨류값들을 모두 아우른다. if 문을 써서 있으면 참 없으면 거짓인 조건문을 만든다.
    print("정답입니다.")
else:
    print("오답입니다.")


# In[ ]:




