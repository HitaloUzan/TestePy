#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

stores_merge = pd.read_csv('Store_Merge.csv')
retail_data_w23_merge = pd.read_csv('Retail_Data_W23_Merge.csv')
retail_unlabeled_data_concat = pd.read_csv('Retail_Unlabeled_Data_Concat.csv')
retail_data_orders_merge = pd.read_csv('Retail_Data_Orders_Merge.csv')

display(stores_merge)
display(retail_data_w23_merge)
display(retail_unlabeled_data_concat)
display(retail_data_orders_merge)


# In[4]:


tabela_concat1 = pd.concat([retail_data_w23_merge,retail_unlabeled_data_concat])
display(tabela_concat1)


# In[10]:


tabela_merge1 = pd.merge(tabela_concat1, retail_data_orders_merge, how = 'left', on = "Id", suffixes = ('', '_y'))
display(tabela_merge1)


# In[12]:


tabela_merge2 = pd.merge(tabela_merge1, stores_merge, how = 'left', on = "Store")
display(tabela_merge2)


# In[17]:


tabela_R = pd.read_csv('response_R.csv')
display(tabela_R)
display(tabela_merge2)
tabela_R.equals(tabela_merge2)


# In[ ]:




