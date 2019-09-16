#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request
datos = urllib.request.urlopen('https://www.cotecnova.edu.co').read()


# In[5]:


datos


# In[6]:


import sys


# In[12]:


pip install beautifulsoup4 


# In[15]:


from bs4 import BeautifulSoup
 
soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
    print(tag.get('href'))


# In[18]:


title = BeautifulSoup(datos)
titles = title('title')
print (titles)


# In[19]:


p = BeautifulSoup(datos)
ps = p('p')
print (ps)


# In[ ]:




