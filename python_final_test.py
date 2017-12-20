
# coding: utf-8

# In[1]:


def add(x, y):
    return x+y


# In[2]:


x = {1, 2, 3}
list(x)


# In[3]:


#### Pandas

##### pandas로 product_airtime.csv에서 첫 10줄만 읽어들이려고 한다. 
##### pandas 공식 문서를 참고하여 해당하는 코드를  작성하라.


# In[4]:


import pandas as pd
pd.read_csv("product_airtime.csv", nrows = 10)


# In[5]:


#### 컬럼평균
##### product_airtime.csv에서 ONAIR_MINS 컬럼의 평균을 구하는 코드를 작성하라.


# In[6]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air["ONAIR_MINS"].mean()


# In[7]:


#### 선택
##### product_airtime.csv에서 10번 행부터 20번 행까지, ONAIR_START_TMS와 
##### ONAIR_END_TMS 컬럼을 보여주는 코드를 작성하라.


# In[8]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air.loc[10:21, ["ONAIR_START_TMS", "ONAIR_END_TMS"]]


# In[9]:


#### 정렬
##### product_airtime.csv에서 ONAIR_MINS가 가장 짧은 5행을 보여주는 코드를 작성하라.


# In[10]:


import pandas as pd
air = pd.read_csv("product_airtime.csv")
air["ONAIR_MINS"].sort_values().iloc[0:6]


# In[11]:


#### 필터:비교
##### product_airtime.csv에서 ONAIR_MINS가 0.1보다 작은 행을 보여주는 코드를 작성하라

import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[air["ONAIR_MINS"] < 0.1]


# In[12]:


#### 필터:날짜
##### product_airtime.csv에서 ONAIR_DATE가 2015-02-04인 행을 보여주는 코드를 작성하라
import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[air["ONAIR_DATE"] == "2015-02-04"]


# In[13]:


#### isnull
##### product_airtime.csv에서 HOST1과 HOST2가 모두 있는 행을 보여주는 코드를 작성하라 

import pandas as pd
air = pd.read_csv("product_airtime.csv")
air[(~air["HOST1"].isnull()) & (~air["HOST2"].isnull())]


# In[14]:


air[~((air["HOST1"].isnull()) | (air["HOST2"].isnull()))]


# In[15]:


#### groupby, mean
##### product_airtime.csv 에서 PRODUCT_NBR 별로 ONAIR_MINS 의 평균을 구하는 코드를 작성하라
import pandas as pd
air = pd.read_csv("product_airtime.csv")
air.groupby("PRODUCT_NBR")["ONAIR_MINS"].mean()


# In[16]:


#### groupby, filter
#### product_airtime.csv 에서 PRODUCT_NBR별로 그룹을 짓고, 10행 이상을 가진 그룹을 골라, 그 그룹 내에 
#### 속한 행을 보이는 코드를 작성하라

import pandas as pd
air = pd.read_csv("product_airtime.csv")
group = air.groupby("PRODUCT_NBR")
group.filter(lambda group : len(group) > 10)


# In[17]:


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


# In[18]:


import numpy as np


# In[19]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")


# In[20]:


iris.head()


# In[21]:


## distplot
get_ipython().magic('matplotlib inline')
import seaborn as sns
plot = sns.distplot(iris["petal_length"], vertical = True, hist=False)


# In[22]:


## regplot
get_ipython().magic('matplot inline')
import seaborn as sns
sns.regplot(x = iris["sepal_length"],
           y = iris["petal_length"],
           fit_reg = False,
           color = "red")


# In[23]:


get_ipython().magic('matplotlib inline')
import seaborn as sns

sns.barplot(x=iris["species"], y=iris["sepal_length"], ci=None)


# In[24]:


get_ipython().magic('matplotlib')
import seaborn as sns

g = sns.FacetGrid(iris, col = "species")
g.map(sns.distplot, "petal_length")


# In[25]:


## PairGrid
get_ipython().magic('matplotlib inline')
import seaborn as sns
g = sns.PairGrid(iris, hue="species")
g.map(sns.regplot, fit_reg=False)


# In[28]:


import statsmodels.formula.api as smf
results = smf.ols("petal_length ~ sepal_length + sepal_width",
                 data = iris).fit()
results.summary()

