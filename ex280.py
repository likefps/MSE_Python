#!/usr/bin/env python
# coding: utf-8

# In[1]:


#280번문제
import random # 랜덤함수를 불러오


class Account:
    # class variable
    account_count = 0  # 초기값 0으로 바인딩 

    def __init__(self, name, balance):#함수설정
        self.deposit_count = 0  # 객체가 생성될때 카운트 해주는 변수처음 0번
        self.deposit_log = []  #  비어있는 리스트  저장하려고.. 
        self.withdraw_log = []#  비어있는 리스트

        self.name = name
        self.balance = balance
        self.bank = "SC은행"  

        
        num1 = random.randint(0, 999)  # 계좌번호를 만드는 것 3자리 2자리 6자리 랜덤 계좌번호를 만든다.
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 문자열로 변경 .. --> 3자리로 바꿔줌 (zfill) 
        num2 = str(num2).zfill(2)  # 문자열로 변경 .. --> 2자리로 바꿔줌 (zfill)
        num3 = str(num3).zfill(6) # 문자열로 변경 .. --> 6자리로 바꿔줌 (zfill)
        self.account_number = num1 + '-' + num2 + '-' + num3  # 3자리 - 2자리- 6자리 계좌번호 완성
        Account.account_count += 1  # 계좌가 만들어질때마다 account_count 값이 1씩 증가함.

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):  # 인스턴스 메소드 형태로 self ,, 입금액을 amount로 바운딩
        if amount >= 1: # 입금액이 1원 이상이면 
            self.deposit_log.append(amount) # 입금이 일어날때마다 저장
            self.balance += amount  # 잔고에다가 입금액을 더해주면 된다.

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:   # 증가된 카운트 값이 5의 배수이면 이때 이자를 지급      
                
                self.balance = (self.balance * 1.01) # 1프로의 이자를 지급하겠다.


    def withdraw(self, amount):
        if self.balance > amount:  # 잔고가 출금액보다 많아야 출금이 가능하게 설정.
            self.withdraw_log.append(amount)  # 출금이 일어날때마다 그것을 저장해주는 리스트
            self.balance -= amount  # 출금은 잔고에서 빠져나가는것 이니까. 

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount) # 출금한 금액을 가져와서 출력

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)  # 입금액 출력


k = Account("Kim", 1000)
k.deposit(100) # 예금액 100원 ,200원, 300원
k.deposit(200) 
k.deposit(300)
k.deposit_history() # 입금기록

k.withdraw(100)  # 출금액 100원 200원
k.withdraw(200)
k.withdraw_history() # 출금기록


# In[ ]:




