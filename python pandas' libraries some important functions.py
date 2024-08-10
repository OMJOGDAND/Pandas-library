#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[11]:


customer=pd.read_csv(r"C:\Users\jogda\Downloads\customers.csv")


# In[13]:


customer.head(5)


# In[14]:


# reading from url


# In[15]:


df_url=pd.read_csv('https://raw.githubusercontent.com/kimfetti/Videos/master/Pandas_Tips/data/customers.csv')


# In[17]:


df_url.head(5)


# In[18]:


# if we dont want to creat a new colum we can simply
# do index_col= and we can use as your wish colum


# In[19]:


df=pd.read_csv('https://raw.githubusercontent.com/kimfetti/Videos/master/Pandas_Tips/data/customers.csv',index_col='ID')


# In[20]:


df.head(5)


# In[21]:


df.info()


# In[22]:


df['Phone'].value_counts()


# In[23]:


df.LTV.value_counts()


# In[24]:


# if there are missing values we can use 


# In[25]:


df=pd.read_csv('https://raw.githubusercontent.com/kimfetti/Videos/master/Pandas_Tips/data/customers.csv',
                index_col='ID',na_values='?',nrows=100)


# In[28]:


df.shape


# In[29]:


# we can now import excel data and we are going to do some operations on it


# In[55]:


excel=pd.read_excel(r"C:\Users\jogda\Downloads\store_data.xlsx",sheet_name='purchases',skiprows=1,skipfooter=1,thousands=',',true_values=['Yes'],false_values=['no'])
# in this case we have to mention sheet name bacause by default pandas get first sheet
# in the excel sheet there can be a no of sheets presentd you have to mention which one is needed


# In[56]:


excel


# ### skip unnecessary rows: skiprows(header)

# In[57]:


excel.head()


# In[58]:


excel.tail()


# In[ ]:





# In[59]:


excel.Online.value_counts()


# In[63]:


excel[excel['Online']=='No'].value_counts()


# In[64]:


# rename the colomn names 


# In[65]:


pd.__version__


# In[66]:


df


# In[67]:


df.head()


# In[68]:


df.rename(columns={'First Name':'first_names'})


# In[70]:


df.rename({'First Name':'first_name'},axis=1)


# In[72]:


df.rename(index={4576:'4576_sophia'})


# In[74]:


# updating pandas data type


# ### Create Data

# In[75]:


data_dict={
    'cost':[25,19,88],
    'sale_price':[20,19,59]
}
df=pd.DataFrame(data=data_dict)


# In[78]:


df


# ### Basics

# #### Change the data type of entire dataframe

# In[77]:


df.astype('float').dtypes


# In[79]:


df.sale_price.dtype


# In[80]:


df.sale_price.astype(float)


# In[81]:


df.sale_price.astype(float).dtype


# # mapper
# ## changing the data type of one column with the mapper
# ### just like other pandas method(like rename),you can pass a mapper to astype in style:
# #### {column_name:new_data_type}

# In[84]:


df


# In[86]:


df.astype({'sale_price':'float'}).dtypes


# # dropping a column

# In[92]:


excel.head()


# In[94]:


excel.drop('Online',axis=1)


# In[97]:


excel.drop(columns='Cost')


# In[100]:


excel.drop(index=0)


# In[101]:


# drop multiple columns 


# In[103]:


excel.drop(columns=['Customer ID','Online'])


# In[104]:


### Dropping information permanantly


# In[105]:


excel.drop(columns='Online',inplace=True)

# inplace command actualy delete data when inplace is used the data is permanantly looosee


# ##  pandas tips:dropna()

# In[106]:


pet_data=pd.read_csv('https://raw.githubusercontent.com/kimfetti/Videos/master/Pandas_Tips/data/pet_data.csv')


# In[107]:


pet_data.head()


# In[109]:


pet_data.info()


# In[110]:


pet_data.dropna()


# In[112]:


pet_data.dropna().shape


# In[113]:


pet_data.dropna().info()


# In[114]:


### Drop rows missing all values


# In[115]:


pet_data.dropna(how='all')


# In[116]:


pet_data.dropna(how='all').shape


# In[117]:


pet_data.dropna(how='all').info()


# In[118]:


pet_data.head()


# In[119]:


pet_data.dropna(subset='name')


# In[120]:


pet_data.dropna(subset='name').info()


# In[123]:


pet_data.dropna(subset=['name','pet_type'],how='all')


# In[125]:


pet_data.dropna(subset=['name','pet_type']).info()


# In[126]:


pet_data.dropna(subset=['name','pet_type'],how='all')


# ### Drop columns with missings

# In[128]:


pet_data.head()


# In[130]:


pet_data.dropna(axis=1)

# this is happen because in our data each column have a missing value 
# thats why dropna function drop the all columns


# In[132]:


pet_data.dropna(axis=1,how='all')


# ### set threshold for number of missings

# In[134]:


missing_threshold=pet_data.shape[0]*.5
missing_threshold


# In[136]:


pet_data.dropna(axis=1,thresh=missing_threshold)


# In[138]:


pet_data.isna().sum()


# ## Make permanant change

# In[139]:


pet_data.dropna(how='all',inplace=True)


# In[140]:


pet_data


# ### Drop blank rows

# In[141]:


pet_data.shape


# ### Find duplicate rows/drop dupllicate 

# In[142]:


pet_data.duplicated()


# In[143]:


pet_data[pet_data.duplicated(keep=False)]


# In[145]:


pet_data[pet_data.duplicated()]


# In[146]:


pet_data.drop_duplicates()


# In[147]:


no_dupes=pet_data.drop_duplicates()


# In[148]:


no_dupes[no_dupes.duplicated()]


# In[149]:


pet_data.head()


# In[150]:


pet_data.name.value_counts()


# In[151]:


pet_data.drop_duplicates(subset='name')


# In[153]:


pet_data.drop_duplicates(subset='name').name.value_counts()


# In[154]:


pet_data.drop_duplicates(subset=['name','pet_type'])


# In[155]:


pet_data.drop_duplicates(subset=['name','pet_type']).value_counts()


# ### specify which duplicate to keep

# In[156]:


pet_data.drop_duplicates(subset='name')


# In[157]:


pet_data.drop_duplicates(subset='name',keep='last')


# In[159]:


pet_data.drop_duplicates(subset='name',keep=False)


# In[160]:


pet_data.name.value_counts()


# ### Make permanant changes

# In[161]:


pet_data.drop_duplicates().shape


# In[162]:


pet_data.drop_duplicates(inplace=True)


# In[163]:


pet_data.shape


# In[ ]:




