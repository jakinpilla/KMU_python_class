
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


air = pd.read_csv('product_airtime.csv')
air.head()


# In[3]:


air['ONAIR_MINS'].sum()


# In[4]:


air['ONAIR_MINS'].mean()


# In[5]:


air['ONAIR_MINS'].count()


# In[6]:


air.groupby("PRODUCT_NBR")["ONAIR_MINS"].count()


# In[7]:


air.groupby('ONAIR_DATE')["ONAIR_MINS"].mean()


# In[9]:


air.groupby(["PRODUCT_NBR", "ONAIR_DATE"])["ONAIR_MINS"].sum()


# In[14]:


grouped = air.groupby(["PRODUCT_NBR", "ONAIR_DATE"])


# In[16]:


host_group =air.groupby(["HOST1", "ONAIR_DATE"])


# In[17]:


grouped["ONAIR_MINS"].sum()


# In[18]:


grouped["ONAIR_MINS"].agg([sum, len])


# In[19]:


import numpy as np


# In[26]:


res = grouped["ONAIR_MINS"].agg([sum, np.mean, np.std])


# In[27]:


res.to_csv("sum.csv")


# In[28]:


res.to_clipboard


# In[29]:


min_sums = res["sum"]


# In[30]:


min_sums


# In[33]:


host = air.groupby(["PRODUCT_NBR", "HOST1"])["ONAIR_MINS"].sum()


# In[34]:


host


# In[35]:


host.groupby("PRODUCT_NBR").apply(lambda x: x / x.sum())


# In[36]:


pd.pivot_table(
    air, 
    columns="PRODUCT_NBR",
    index="HOST1",
    values="ONAIR_MINS",
    aggfunc=np.sum,
    fill_value=0
)


# In[37]:


pd.options.display.max_rows = 15


# In[38]:


product = pd.read_csv("product_master.csv")


# In[39]:


pd.merge(air, product, on="PRODUCT_NBR")


# In[40]:


prod_sum = air.groupby("PRODUCT_NBR")["ONAIR_MINS"].agg([sum])


# In[41]:


prod_sum


# In[42]:


product[product["PRODUCT_CATEGORY"]=="Fun & Leisure"]


# In[43]:


pd.merge(prod_sum.reset_index(), product, on="PRODUCT_NBR")

