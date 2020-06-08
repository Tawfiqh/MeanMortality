#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd

df_all = pd.read_csv("226786564.csv", skiprows=8, nrows=21, usecols=[0,1])
display(df_all)


# In[58]:


df_male = pd.read_csv("226786564.csv", skiprows=48, nrows=21, usecols=[0,1])
display(df_male)


# In[59]:


df_female = pd.read_csv("226786564.csv", skiprows=88, nrows=22, usecols=[0,1])
display(df_female)


# In[82]:


def graph(df):
    display(df)
    df['age_trimmed']=df['Age'].str.slice(start=5)
#     df.drop('Age')
    df.set_index('age_trimmed').plot.bar(rot=0, figsize=[20,10])

    
    

df_all['Male'] = df_male['Total mortality']
df_all['Female'] = df_female['Total mortality']


graph(df_all.drop(0))


# In[83]:


graph(df_male.drop(0))
graph(df_female.drop(0))


# In[ ]:




