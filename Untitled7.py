#!/usr/bin/env python
# coding: utf-8

# In[1]:


#QUESTION 1
class Robot:
	def __init__(self, position=[0, 0]):
		self.position = position
		print(self)
	
	def __repr__(self):
		return "\nRobot Position: {0}".format(self.position)
	
	def move(self, steps):
		for step in steps:
			if step == "R":
				print("(right)")
				self.position[0] += 1
			elif step == "L":
				self.position[0] -= 1
				print("(left)")
			elif step == "U":
				self.position[1] += 1
				print("(up)")
			elif step == "D":
				self.position[1] -= 1
				print("(down)")
			else:
				print("(idle)")
			print(self)

r = Robot()
r.move("UUULDDRRURDDLL")


# In[2]:


#question 2
company_data = ['book','pencil','pen','note book','sharpener','rubber']
item = input('what item do you want to check in the bag')


for i in range(1):
    if item in company_data:
        print('Item is in company data')
        break
    else:
        print("data is not available")


# In[3]:


#question 3
from datetime import datetime


def get_part_of_day(hour):
    return (
        "light" if 5 <= hour <= 18
        else
        "dark"
    )


h = datetime.now().hour

print(f"Its {get_part_of_day(h)}  right now.")


# In[8]:


#question 4
from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)


# In[4]:


#question 5
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the cash_credit, cash_withdraw & change_password Machine")

    def cash_credit(self):
        amount=float(input("Enter amount to be cash_credit: "))
        self.balance += amount
        print("\n Amount cash_credit:",amount)

    def cash_withdraw(self):
        amount = float(input("Enter amount to be cash_Withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You cash_Withdraw:", amount)
    def change_password(self):
        amount = float(input("change_password: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You change_password:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.cash_credit()
s.cash_withdraw()
s.change_password
s.display()


# In[5]:


#question 6
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# In[6]:


#question 7
# Python 3 program to find
# factorial of given number
def factorial(n):
	
	# Checking the number
	# is 1 or 0 then
	# return 1
	# other wise return
	# factorial
	if (n==1 or n==0):
		
		return 1
	
	else:
		
		return (n * factorial(n - 1))

# Driver Code
num = 8;
print("number : ",num)
print("Factorial : ",factorial(num))


# In[7]:


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# In[8]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# In[20]:


phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))


# In[4]:


lines = []
while True:
    s = input("Enter Lines :")
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)
# Leave input blank to stop


# In[5]:


phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))


# In[6]:


items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))


# In[7]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[8]:


# Python code to demonstrate use
# of math.fsum() function

# fsum() is found in math library
import math

# range(10)
print(math.fsum(range(10)))

# Integer list
arr = [1, 4, 6]
print(math.fsum(arr))

# Floating point list
arr = [2.5, 2.4, 3.09]
print(math.fsum(arr))


# In[ ]:




