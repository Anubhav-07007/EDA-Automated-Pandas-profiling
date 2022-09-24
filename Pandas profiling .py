#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

from pandas_profiling import ProfileReport


# In[2]:


df=pd.read_csv(r'D:\Project working\New_Entertainer_Breakthrough.csv')


# In[3]:


df.columns


# In[6]:


df.drop(['Unnamed: 0'],axis=1,inplace=True)


# In[10]:


profile=ProfileReport(df,title='EDA',html={'style':{'full_width':True}})


# In[11]:


profile


# In[ ]:




