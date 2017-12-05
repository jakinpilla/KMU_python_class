
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


# In[17]:


air[air["PRODUCT_NBR"] == "P150000002"]


# In[18]:


grouped["ONAIR_MINS"].count().sort_values(ascending=False)


# In[20]:


import numpy as np


# In[21]:


grouped["ONAIR_MINS"].agg([np.sum, np.mean, np.std, len]).sort_values("sum", ascending=False)


# In[22]:


grouped["ONAIR_MINS"].agg([np.sum, np.mean, np.std, len]).sort_index()


# In[25]:


grouped.agg({
    "ONAIR_DATE" : min,
    "ONAIR_MINS" : [np.sum, np.mean, np.std]
}).sort_values(("ONAIR_MINS", "sum"))


# In[27]:


air[air["ONAIR_MINS"] > 50]


# In[28]:


def over_1_hour(group):
    return group["ONAIR_MINS"].sum() > 60


# In[29]:


len(air)


# In[30]:


air.count()


# In[31]:


grouped.filter(lambda group: len(group) < 5)


# In[33]:


grouped.filter(lambda group: group["ONAIR_DATE"].min() > "2015-03-10")


# In[ ]:


###### select * from (select min(ONAIR_DATE) from air groupby PRODUCT_NBR ) as air_date
###### where air_date.ONAIR_DATE > "2015-03-10"


# In[34]:


air_date = air.groupby("PRODUCT_NBR").agg({"ONAIR_DATE" : min})


# In[37]:


air_date[air_date["ONAIR_DATE"] > "2015-03-10"]


# In[39]:


air[air["ONAIR_DATE"] > "2015-03-10"]


# In[40]:


grouped.filter(lambda group: group["ONAIR_MINS"].count() < 5)


# In[41]:


###### 방송시간 합계가 60분 이상인 제품 그룹
grouped.filter(lambda group: group["ONAIR_MINS"].sum() > 60)


# In[42]:


grouped.filter(over_1_hour)


# In[43]:


## lambda 함수
grouped.filter(lambda group: group["ONAIR_MINS"].sum() > 60)


# In[44]:


## groupby level
min_sums


# In[45]:


min_sums.groupby(level=0)


# In[46]:


min_sums.groupby(level=0).agg(np.sum)


# In[47]:


min_sums.groupby(level=0).sum()


# In[48]:


## apply
min_sums.groupby(level=0).apply(lambda x: x / x.sum())


# In[49]:


## reset index
min_sums.reset_index()


# In[50]:


## pivoting

pvt = pd.pivot_table(
    air,
    columns = "ONAIR_DATE",
    index="PRODUCT_NBR",
    values="ONAIR_MINS",
    aggfunc=numpy.sum
)


# In[52]:


pvt.head(10)


# In[54]:


pvtz = pvt.fillna(0)
pvtz.head(10)


# In[55]:


pd.pivot_table(
    air, 
    columns="ONAIR_DATE",
    index="PRODUCT_NBR",
    values="ONAIR_MINS",
    aggfunc=  np.sum,
    fill_value=0
)

