#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


new = pd.read_csv('Hour Distribution.csv')
new.head()


# In[3]:


new.dtypes


# In[4]:


data = new.drop(['weektype','Total_Teacher_Slots','Total_Trial_Completions','Total_Paid_Completions'], axis=1)
data.head()


# In[5]:


data.dtypes


# In[7]:


plt.figure(figsize=(15,6))
sns.barplot(x='dayhour', y='Paid_Bookings', data=data.iloc[1:25])
plt.show()


# In[8]:


plt.figure(figsize=(15,6))
sns.barplot(x='dayhour', y='Total_Trial_Bookings', data=data.iloc[1:25])
plt.show()

