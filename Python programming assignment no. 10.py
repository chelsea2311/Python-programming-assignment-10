#!/usr/bin/env python
# coding: utf-8

# PYTHON BASIC PROGRAMMING ASSIGNENT NO. 10

# In[2]:


#Q1.
## Input from user
l=[]
for i in range(5):
    l.append(int(input()))
sum = 0
for i in l:
    sum = sum + i
print("sum of list is:",sum)


# In[3]:


#Q2.
## Input from user
l=[]
for i in range(5):
    l.append(int(input()))
prod = 1
for i in l:
    prod = prod * i
print("sum of list is:",prod)


# In[4]:


#Q3.
l=[]
for i in range(5):
    l.append(int(input()))  
smallest = min(l)
print("Smallest element in the list is:",smallest)


# In[5]:


#Q4.
l=[]
for i in range(5):
    l.append(int(input()))  
largest = max(l)
print("Largest element in the list is:",largest)


# In[7]:


#Q5.
l=[]
for i in range(int(input("Enter the number of elements you want to enter in a list: "))):
    l.append(int(input()))
largest=max(l)
l.remove(largest)
sl=max(l)
print("Second largest number is",sl)


# In[8]:


#Q6.
l=[]
for i in range(int(input("Enter the number of elements you want to enter in a list: "))):
    l.append(int(input()))
l.sort(reverse=True)
print("Sorted list",l)
input=int(input("Enter N= "))
l1=l[input- 1]
print("The ",input,"th largest number is =",l1)


# In[9]:


l= [2,3,56,6,4,9]
l.sort()
l[2]


# In[ ]:


#Q7.
l=[]
l1=[]
for i in range(int(input("Enter the number of elements you want to enter in a list: "))):
    l.append(int(input()))
for i in l:
    if i%2==0:
        l1.append(i)
print("Even numbers are: ",l1)       


# In[ ]:


#Q8.
l=[]
l1=[]
for i in range(int(input("Enter the number of elements you want to enter in a list: "))):
    l.append(int(input()))
for i in l:
    if i%2!=0:
        l1.append(i)
print("Odd numbers are: ",l1)  


# In[16]:


#Q9.
l=[[],[1,2,3],["xyz"],[]]
for i in l:
    l.remove([])
print(l)


# In[18]:


#Q10.
l = [1,2,3,"Hello",True,[0.786]]
l1=l
print(l1,l)


# In[ ]:


#Q11.
l=[]
for i in range(5):
    l.append(int(input()))
c=l.count(int(input("The element you want to count: ")))
print("count is",c)

