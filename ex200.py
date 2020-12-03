#!/usr/bin/env python
# coding: utf-8

# In[7]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum=0
for i in ohlc[1:]:  # 2번째부터가 숫자니까 .. 1:   i는 ["open", "high", "low", "close"],[100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310]를 말한다.
    day_profit=i[3]-i[0] # 일짜별 수익은 종가에서 시가를 빼준것 
    sum+=day_profit # 그걸 합계에 누적시켜서 더하면 총 수익이 나온다.
print(sum)

    
    


# In[ ]:




