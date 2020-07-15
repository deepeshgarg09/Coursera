#!/usr/bin/env python
# coding: utf-8

# In[ ]:


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
l=list()
for a in filenames :
  index=a.find(".")
  
  if a[index+1:]=="hpp":
    a =a[:index+1]+"h"
    
    l.append(a)
  else :
    l.append(a)
print(l)    
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

