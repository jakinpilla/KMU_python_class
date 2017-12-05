
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


air = pd.read_csv('product_airtime.csv')


# In[3]:


air.head()


# In[4]:


air['ONAIR_MINS']


# In[5]:


air['ONAIR_MINS'].mean()


# ##### groupby

# ###### select sum(ONAIR_MINS) from air groupby PRODUCT_NBR

# In[6]:


air.groupby('PRODUCT_NBR')['ONAIR_MINS'].sum()


# In[8]:


air.groupby("PRODUCT_NBR")["ONAIR_MINS"].sum().sort_values()


# In[10]:


air.groupby("PRODUCT_NBR")["ONAIR_MINS"].sum().sort_values(ascending = False)


# In[12]:


min_sums = air.groupby(['PRODUCT_NBR', "ONAIR_DATE"])["ONAIR_MINS"].sum()


# In[13]:


min_sums


# In[14]:


grouped = air.groupby('PRODUCT_NBR')


# In[16]:


grouped.get_group("P150000002")

