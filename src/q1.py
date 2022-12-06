#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from statistics import mean
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt


# In[137]:


df = pd.read_json('test.json', lines=True)


# In[139]:


df['gender'] = df.apply(lambda row: row.treatment.get('gender'), axis=1)
df['ethnicity'] = df.apply(lambda row: row.treatment.get('ethnicity'), axis=1)


# In[140]:


def price_row(row):
    if len(row['ranking'])>0:
        if 'price' in row['ranking'][0]:
            return row['ranking']
    else:
        return '0'


# In[141]:


df['position'] = df.apply(lambda row: price_row(row), axis=1)


# In[142]:


df = df[['scraper','gender','ethnicity','position']]
df = df.dropna()


# In[143]:


def price(row):
    ls = []
    for i in row['position']:
        if i is not None and type(i) is dict:
            pc = i.get('price')
            if 'K' in pc:
                pc = pc.replace('K','000')
            if '+' in pc:
                pc = pc.replace('+','')   
            iprice = int(pc.replace(',', '')[1:])
            ls.append(iprice)
    return ls


# In[144]:


df['price'] = df.apply(lambda row: price(row) , axis=1)


# In[145]:


def locate(row):
    for i in row['position']:
        if i is not None and type(i) is dict:
            lo = i.get('locality')
            if lo is not None:
                if 'Champaign' in lo or 'CHAMPAIGN' in lo:
                    return 'Champaign'
                elif 'Chicago' in lo or 'CHICAGO' in lo:
                    return 'Chicago'
                else:
                    return None


# In[146]:


df['locality'] = df.apply(lambda row:locate(row),axis=1)


# In[147]:


df = df.dropna()
df = df.reset_index(drop=True)


# In[148]:


df['price_mean'] = df.apply(lambda row: round(mean(row['price'])) , axis=1)


# In[ ]:





# In[149]:


average_price_groups = df.groupby(['scraper','locality','gender', 'ethnicity']).agg({'price_mean': ['mean']}).astype(int)


# In[150]:


average_price_groups


# In[158]:


model_R = ols('price_mean ~ C(gender) + C(ethnicity) + C(gender):C(ethnicity)', data=df).fit()


# In[159]:


sm.stats.anova_lm(model, typ=2)


# In[151]:


Realtor = df[df.scraper == 'Realtor']


# In[152]:


model_R = ols('price_mean ~ C(gender) + C(ethnicity) + C(gender):C(ethnicity)', data=Realtor).fit()


# In[153]:


sm.stats.anova_lm(model_R, typ=2)


# In[154]:


Trulia = df[df.scraper == 'Trulia']


# In[155]:


model_T = ols('price_mean ~ C(gender) + C(ethnicity) + C(gender):C(ethnicity)', data=Trulia).fit()


# In[156]:


sm.stats.anova_lm(model_T, typ=2)


# In[160]:


fig = interaction_plot(x=df['ethnicity'], trace=df['gender'], response=df['price_mean'], 
    colors=['#d17a22', '#4c061d'])
plt.show()


# In[164]:


df[['rank1','rank2','rank3','rank4','rank5','rank6','rank7','rank8','rank9','rank10']] = pd.DataFrame(df.price.tolist(), index= df.index)


# In[173]:


gender_ranks = df.groupby(['gender']).agg({'rank1': ['mean'],'rank2': ['mean'],'rank3': ['mean'],'rank4': ['mean'],
                                           'rank5': ['mean'],'rank6': ['mean'],'rank7': ['mean'],'rank8': ['mean'],
                                           'rank9': ['mean'],'rank10': ['mean']}).astype(int)
gender_ranks


# In[189]:


gender_ranks.T.plot()
plt.xlabel('Ranking')
plt.ylabel('Average Price')


# In[174]:


ethnicity_ranks = df.groupby(['ethnicity']).agg({'rank1': ['mean'],'rank2': ['mean'],'rank3': ['mean'],'rank4': ['mean'],
                                           'rank5': ['mean'],'rank6': ['mean'],'rank7': ['mean'],'rank8': ['mean'],
                                           'rank9': ['mean'],'rank10': ['mean']}).astype(int)
ethnicity_ranks


# In[190]:


ethnicity_ranks.T.plot()
plt.xlabel('Ranking')
plt.ylabel('Average Price')


# In[ ]:




