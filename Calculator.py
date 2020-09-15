#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
s = input()
b = int(input())

if s == '//':
    print(a//b)
elif s == '**' or "^":
    print(a**b)
elif s == '+':
    print(a+b)
elif s == '-':
    print(a-b)
elif s == '*':
    print(a*b)
elif s == '/':
    print(a/b)
elif s == '%':
    print(a%b)

