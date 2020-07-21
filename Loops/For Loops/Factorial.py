#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorial(n):
    result = 1
    x=1
    while x<=n :
        result = result * x
        x=x+1
    return result

for n in range(10):
    print(n, factorial(n))

