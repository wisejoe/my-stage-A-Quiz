#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[6]:


fbs = pd.read_csv('C:/Users/ENGR JOSEPH/Desktop/Hamoye/FoodBalanceSheets_E_Africa_NOFLAG dataset.csv')


# In[7]:


arr =([[94, 89, 63], [93, 92, 48], [92, 94, 56]])


# In[8]:


s = [['him', [90, 28, 43]]]


# In[9]:


s[0][1][1]


# In[10]:


my_tuppy = (1,2,5,8)


# In[12]:


my_tuppy[2] = 6


# In[13]:


fbs


# In[16]:


fbs.groupby('Element')['Y2014'].sum()


# In[15]:


fbs.describe()


# In[17]:


fbs.isnull().sum()


# In[18]:


fbs.groupby('Element').sum()


# In[19]:


fbs.groupby('Element')['Y2014', ].sum().sum()


# In[ ]:




