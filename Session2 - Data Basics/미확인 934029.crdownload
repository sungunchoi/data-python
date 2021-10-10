#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import psycopg2
from sqlalchemy import create_engine


# ### 2. 데이터 불러오기

# In[26]:


indata =     pd.read_csv("../dataset/kopo_decision_tree_all_new.csv")


# In[27]:


indata.shape


# ### 3. 데이터 처리 (컬럼 소문자로 변환)

# In[29]:


indata.columns = indata.columns.str.lower()


# ### 4. 데이터 저정하기

# In[31]:


targetDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopodb"


# In[32]:


targetDbPrefix = "postgresql://"


# In[33]:


targetUrl = "{}{}:{}@{}:{}/{}".format(targetDbPrefix,
                                      targetDbId,
                                      targetDbPw,
                                      targetDbIp,
                                      targetDbPort,
                                     targetDbName)


# In[34]:


pg_kopo_engine = create_engine(targetUrl)








# In[38]:


tableName = "pgout_kopo_sc"


# In[39]:


indata.to_sql(name=tableName, 
             con = pg_kopo_engine,
             if_exists="replace", index=False)










