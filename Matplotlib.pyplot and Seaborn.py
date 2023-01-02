#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as snd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from numpy.random import randn


# In[3]:


df=pd.DataFrame(randn(10,4),columns=['a','b','c','d'])


# In[4]:


df.plot(kind='bar')


# In[6]:


sns.get_dataset_names()


# In[7]:


iris=sns.load_dataset('iris')
iris


# In[10]:


iris.sepal_length.plot(kind='hist',bins=30)


# In[11]:


df=iris.drop(columns=['species'],axis=1)


# In[17]:


df.hist(color='r',figsize=(20,15),bins=50)


# In[19]:


plt.figure(figsize=(13,5))
ax=sns.boxplot(data=df)
plt.yticks(range(5,60,5))
plt.xlabel('salary and Monthly Rupees')
plt.show()


# In[21]:


df1=pd.DataFrame({'Age_years':[23,45,65,23,14,34,62,78,44,23,12,34],
                'Salary_thoushands':[54,65,67,45,78,97,56,77,45,66,88,98]})


# In[23]:


plt.figure(figsize=(15,20))
ax=sns.boxplot(data=df1)
plt.yticks(range(5,60,5))
plt.xlabel('salary and Monthly Rupees')
plt.show()


# In[24]:


q1=df1.quantile(0.25)
print('q1-',q1)


# In[25]:


q2=df1.quantile(0.50)
print('q2-',q2)


# In[26]:


q3=df1.quantile(0.75)
print('Q3',q3)


# In[27]:


iqr=q3-q1
print('iqr-',iqr)


# In[30]:


from pandas.plotting import scatter_matrix


# In[31]:


scatter_matrix(df,figsize=(5,6),color='r',diagonal='kde')


# In[33]:


df2=sns.load_dataset('iris')
df2


# In[35]:


scatter_matrix(df2,figsize=(20,15),color='r',diagonal='kde')


# In[36]:


Rupees_monthly=[2000,2350,900,15000,1500]
items=['Tution_Fees','Mobile_number','Electicity_bill','Rent','Music']


# In[37]:


plt.pie(x=Rupees_monthly,labels=items)
plt.show()


# In[38]:


plt.figure(figsize=(8,9))
plt.pie(x=Rupees_monthly,labels=items,explode=[0.3,0,0,0,0],autopct='%0.2f',rotatelabels=True) 
plt.show()       


# In[39]:


tip=sns.load_dataset('tips')
tip


# In[46]:


sns.relplot(x='total_bill',y='tip',data=tip)


# In[50]:


sns.relplot(x='total_bill',y='tip',data=tip,hue='smoker',style='time')


# In[51]:


sns.scatterplot(x='total_bill',y='tip',data=tip,hue='smoker',style='time')


# In[52]:


sns.lineplot(x='total_bill',y='tip',data=tip,hue='smoker',style='time')


# In[3]:


tip=sns.load_dataset('tips')
tip


# In[5]:


sns.catplot(x='day',y='total_bill',data=tip)


# In[6]:


sns.swarmplot(x='day',y='total_bill',data=tip)


# In[7]:


sns.countplot(x='day',data=tip)


# In[10]:


plt.figure(figsize=(20,15))
plt.grid()
sns.countplot(x='size',hue='time',data=tip)
plt.yticks(range(5,100,5))
plt.show()


# In[11]:


sns.stripplot(x='day',y='total_bill',data=tip)


# In[12]:


sns.stripplot(x='smoker',y='total_bill',data=tip)


# In[13]:


x=randn(1000)


# In[14]:


sns.distplot(x)
plt.show()


# In[15]:


sns.kdeplot(x)


# In[17]:


sns.jointplot(x=tip['total_bill'],y=tip['tip'])


# In[19]:


sns.regplot(x='tip',y='total_bill',data=tip)


# In[20]:


sns.lmplot(x='tip',y='total_bill',data=tip)


# In[ ]:




