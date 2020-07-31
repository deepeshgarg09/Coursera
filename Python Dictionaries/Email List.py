#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def email_list(domains):
	emails = []
	for d,users in domains.items():
        
	    for user in users:
            
	        emails.append(user+'@'+d)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

