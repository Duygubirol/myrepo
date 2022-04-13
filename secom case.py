#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
path1='https://raw.githubusercontent.com/hinatanvir/Fault-Detection-SECOM/main/secom.data?token=GHSAT0AAAAAABTMJQPCMEYJ4LIGT2V6TRG2YSS5ZWA'
data = pd.read_csv(path1,delimiter=' ',header=None)
data


# In[5]:


path2='https://raw.githubusercontent.com/hinatanvir/Fault-Detection-SECOM/main/secom_labels.data?token=GHSAT0AAAAAABTMJQPCJP4OZMM573LK4Q7UYSS562A'
label=pd.read_csv(path2,delimiter=' ',header=None)
label


# In[6]:


data.columns = ['feature'+str(x+1) for x in range(len(data.columns))]
data


# In[ ]:




