#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[3]:


# Program to sort alphabetically the words form a string provided below

my_str = "Hello this Is England"


# breakdown of the string into a list of words
words = [word.lower() for word in my_str.split()]

# sorting the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


# In[7]:


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")


# In[9]:


alpha,string=0,"worldcup2023"
for i in string:
	if (i.isalpha()):
		alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)


# In[11]:


# Python3 code to demonstrate
# checking a number is palindrome
# using str() + string slicing

# initializing number
test_number = 100000000

# printing the original number
print ("The original number is : " + str(test_number))

# using str() + string slicing
# for checking a number is palindrome
res = str(test_number) == str(test_number)[::-1]

# printing result
print ("Is the number palindrome ? : " + str(res))


# In[ ]:




