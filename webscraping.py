#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


# In[3]:


import requests as reqs
from bs4 import BeautifulSoup


# In[4]:


url='https://www.flipkart.com/search?q=moblie&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=moblie%7CMobiles&requestId=156f0e12-206d-440c-b67d-7990d2a8d445&as-searchtext=moblie'


# In[5]:


req=requests.get(url)


# In[6]:


content=BeautifulSoup(req.content,'html.parser')


# In[7]:


print(req)


# In[8]:


print(content)


# In[9]:


name=content.find_all('div',{"class":"_4rR01T"})
price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
rating=content.find_all('div',{"class":"_3LWZlK"})


# In[10]:


print(name)


# In[11]:


print(price)


# In[12]:


print(rating)


# In[13]:


print(name[0])


# In[14]:


print(price[0])


# In[15]:


print(rating[0])


# In[16]:


nm=[]
rt=[]
pr=[]
for i in name:
    nm.append(i.text)
for i in price:
    pr.append(i.text)
for i in rating:
    rt.append(i.text)


# In[17]:


data={'NAME':nm,'PRICE':pr,'RATING':rt}
df=pd.DataFrame(data)
print(df)


# In[18]:


print(data)


# In[19]:


print(nm)


# In[40]:


len(nm)


# In[41]:


len(rt)


# In[42]:


len(pr)


# In[43]:


data={'A':price,'B':rating,'C':name}


# In[44]:


print(data)


# In[45]:


df=pd.DataFrame(data)


# In[46]:


print(df)


# In[47]:


df.isnull().sum().sort_values(ascending=False)


# In[51]:


import numpy as np


# In[52]:


import pandas as pd


# In[57]:


df.head(10)


# In[55]:


df.describe()


# In[56]:


df.dropna(inplace=True)


# In[58]:


print(df)


# In[60]:


import requests
from urllib.error import URLError
link='https://www.flipkart.com/search?q=moblie&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=moblie%7CMobiles&requestId=156f0e12-206d-440c-b67d-7990d2a8d445&as-searchtext=moblie'
try:
    response=requests.get(link)
except URLError as url_error:
    print("server not found")
else:
    print("there is no error")


# In[120]:


df.info()


# In[65]:


df.isna().any()  ##cleaning / filling process for missing


# In[132]:


df.isna()


# In[68]:


df.shape[0]


# In[78]:


df.columns


# In[84]:


round(df.describe(),0)        #to print stat on non numerical data


# In[99]:


df[5:11]                #row indexing


# In[122]:


df['A'].astype(str)


# In[123]:


df['B'].astype(str)


# In[124]:


df['C'].astype(str)


# In[133]:


import warnings                 #data visualization
warnings.filterwarnings("ignore")


# In[142]:


import matplotlib.pyplot as plt
import seaborn as sns
df.columns
df.mode().columns


# In[37]:


df.value_counts()


# In[39]:


df['NAME'].value_counts()


# In[40]:


df['PRICE'].value_counts()


# In[32]:


df['PRICE'].value_counts(normalize=True)


# In[33]:


df[['PRICE','RATING']]


# In[34]:


df.sort_values(by="PRICE")


# In[35]:


df.describe(include=["object"])              #which describes numerical colm


# In[39]:


df.ndim


# In[40]:


df.shape


# In[43]:


df.dtypes


# In[46]:


df['PRICE'].apply(str)


# In[55]:


df.sum()


# In[ ]:




