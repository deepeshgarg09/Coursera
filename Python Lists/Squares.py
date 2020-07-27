#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def squares(start, end):
  a=list()
  while start<=end :
    a.append(start*start)
    start=start+1
    
  return a

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

