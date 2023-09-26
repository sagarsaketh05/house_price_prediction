#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
print("pp")


# In[14]:


data=pd.read_csv('Housing.csv')
print("kk")


# In[15]:


data.head(10)


# In[16]:


data.info()


# In[17]:


data.shape


# In[18]:


data.columns


# In[19]:


data.nunique()


# In[20]:


data.duplicated().sum()


# In[21]:


data.isnull().sum()


# In[24]:


sns.pairplot(data)
plt.show()


# In[25]:


sns.displot(data["price"])
plt.show()


# In[26]:


sns.countplot(data['bedrooms'])
plt.show()


# In[27]:


cat_data=data.select_dtypes(include=["object"]).columns

for column in cat_data:
    un_values=data[column].unique()
    print(f"Unique Values for {column}:{un_values}")


# In[28]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["furnishingstatus"]=le.fit_transform(data["furnishingstatus"])
data["mainroad"]=le.fit_transform(data["mainroad"])
data["guestroom"]=le.fit_transform(data["guestroom"])
data["basement"]=le.fit_transform(data["basement"])
data["hotwaterheating"]=le.fit_transform(data["hotwaterheating"])
data["airconditioning"]=le.fit_transform(data["airconditioning"])
data["prefarea"]=le.fit_transform(data["prefarea"])


# In[29]:


data


# In[30]:


data_s=data.corr()
plt.figure(figsize=(20,15))
sns.heatmap(data_s, annot=True)
plt.show()


# In[31]:


sns.displot(data['price'])
plt.show()


# In[33]:


plt.scatter(data["area"], data["price"])

# Customize the plot
plt.xlabel('Area')
plt.ylabel('Price')
plt.legend(title='Area Category')

# Show the plot
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




