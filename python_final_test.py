
# coding: utf-8

# In[1]:


def add(x, y):
    return x+y


# In[2]:


x = {1, 2, 3}
list(x)


# In[14]:


#### Pandas

##### pandas로 product_airtime.csv에서 첫 10줄만 읽어들이려고 한다. 
##### pandas 공식 문서를 참고하여 해당하는 코드를  작성하라.


# In[4]:


import pandas as pd
pd.read_csv("product_airtime.csv", nrows = 10)


# In[ ]:


#### 컬럼평균
##### product_airtime.csv에서 ONAIR_MINS 컬럼의 평균을 구하는 코드를 작성하라.


# In[7]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air["ONAIR_MINS"].mean()


# In[ ]:


#### 선택
##### product_airtime.csv에서 10번 행부터 20번 행까지, ONAIR_START_TMS와 
##### ONAIR_END_TMS 컬럼을 보여주는 코드를 작성하라.


# In[8]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air.loc[10:21, ["ONAIR_START_TMS", "ONAIR_END_TMS"]]


# In[ ]:


#### 정렬
##### product_airtime.csv에서 ONAIR_MINS가 가장 짧은 5행을 보여주는 코드를 작성하라.


# In[13]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air["ONAIR_MINS"].sort_values().iloc[0:6]


# In[17]:


#### 필터:비교
##### product_airtime.csv에서 ONAIR_MINS가 0.1보다 작은 행을 보여주는 코드를 작성하라

import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[air["ONAIR_MINS"] < 0.1]


# In[19]:


#### 필터:날짜
##### product_airtime.csv에서 ONAIR_DATE가 2015-02-04인 행을 보여주는 코드를 작성하라
import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[air["ONAIR_DATE"] == "2015-02-04"]


# In[24]:


#### isnull
##### product_airtime.csv에서 HOST1과 HOST2가 모두 있는 행을 보여주는 코드를 작성하라 

import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[(~air["HOST1"].isnull()) & (~air["HOST2"].isnull())]


# In[25]:


air[~((air["HOST1"].isnull()) | (air["HOST2"].isnull()))]


# In[27]:


#### groupby, mean
##### product_airtime.csv 에서 PRODUCT_NBR 별로 ONAIR_MINS 의 평균을 구하는 코드를 작성하라
import pandas as pd
air = pd.read_csv("product_airtime.csv")
air.groupby("PRODUCT_NBR")["ONAIR_MINS"].mean()


# In[30]:


#### groupby, filter
#### product_airtime.csv 에서 PRODUCT_NBR별로 그룹을 짓고, 10행 이상을 가진 그룹을 골라, 그 그룹 내에 
#### 속한 행을 보이는 코드를 작성하라

import pandas as pd
air = pd.read_csv("product_airtime.csv")
group = air.groupby("PRODUCT_NBR")
group.filter(lambda group : len(group) > 10)


# In[36]:


## pivot table
## product_master.csv 로 피봇 테이블을 만드는 코드를 작성하라. 행은 BRAND_NAME, 열은 PRODUCT_CATEGORY
## 으로 하라. 각 셀에는 제품의 건수가 들어가도록 하라. 결측값은 0으로 채우라

import pandas as pd
product = pd.read_csv("product_master.csv")
pd.pivot_table(product, 
              columns = "PRODUCT_CATEGORY",
              index = "BRAND_NAME",
              values = "PRODUCT_NBR",
              aggfunc = len,
              fill_value = 0)

