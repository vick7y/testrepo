#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dataset=pd.read_csv('../Ads_research/studyRunTime 2.csv')
dataset['userID']=dataset.userID.astype(int)
dataset['time']=pd.to_datetime(dataset['Timestamp'])


# In[3]:


grouped=dataset.groupby('userID',sort=False)
dic_grouped={}
for key, value in grouped:
    dic_grouped[key]=pd.DataFrame(value).reset_index()


# In[6]:


df_all=pd.DataFrame()
for key in dic_grouped:
    df=dic_grouped[key] #get the dataframe for the specific user
    
    ##create a column called [time_lapse]=time-time(ad_start)
    try:
        time_start=df.time[df[df.event=='start'].index[0]]
    except IndexError:
        print('User '+str(key)+' did not start the ads')
        time_start=df['time'][0]
    df['time_lapse']=df['time']-time_start
    df['time_lapse']=df['time_lapse'].dt.total_seconds()
    df_all=df_all.append(df)


# In[7]:


df_all.head()


# In[9]:


df_all.to_csv('../Ads_research/timelapse2.csv')


# In[ ]:




