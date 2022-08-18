#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[14]:


def hap(g,t,n):
    google=pd.read_csv(g)
    google=google[['STAR','CONTENT']]
    trip=pd.read_csv(t,encoding='UTF-8')
    trip=trip[['별점','리뷰']]
    trip.columns=['STAR','CONTENT']
    hap=google.append(trip).reset_index(drop=True)
    print(hap)
    hap.to_csv(n+'.csv')


# In[16]:


hap("C:/Users/LG-PC/Documents/GitHub/2022_DATA_TEAM5/HS/data/google/Namdaemun Market_Google.csv",
    "C:/Users/LG-PC/Documents/GitHub/2022_DATA_TEAM5/HS/data/tripadvisor/Namdaemun Market_Tripadvisor.csv",'Namdaemun Market.csv')

