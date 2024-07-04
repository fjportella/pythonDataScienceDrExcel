#!/usr/bin/env python
# coding: utf-8

# # Bônus 1 - Automatizando o Uso de Planilhas usando Python
# 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


#base = pd.read_excel(r'E:\Users\quadr\Documents\Projetos\Cursos\Python\Bases\Aula 5\planilha2021-01-02.xlsx')


# In[3]:


import datetime

data_hoje = datetime.date.today()


# In[4]:


data_hoje


# In[5]:


str(data_hoje)


# In[6]:


parte_variavel = '\planilha' +str(data_hoje)
print(parte_variavel)


# In[8]:


datetime.date.today() + datetime.timedelta(days=1)


# In[9]:


base = pd.read_excel(r'E:\Users\quadr\Documents\Projetos\PA-Analytics\Python Básico para Data Science e Analytics\Curso\V2.0\Bases\Bonus 1' +  parte_variavel + '.xlsx')


# In[10]:


base


# In[11]:


base['média_idade'] = pd.Series()
base['média_idade'] = base.Age.mean()


# In[12]:


base


# In[13]:


base['diferença_media'] = pd.Series()

for i in base.index:
    base['diferença_media'][i] = base.Age[i] - base['média_idade'][i]


# In[14]:


base


# In[15]:


base2 = base.dropna(axis = 0, subset=['Age'])

plt.figure(figsize=(20,10))
plt.title('Idade de Homens e Mulheres')
plt.ylabel('Frequência')
plt.xlabel('Idade')

plt.hist(base2[base2.Sex == 'male'].Age, color = 'gray', label = 'homens', alpha = 0.5, edgecolor = 'black')
plt.hist(base2[base2.Sex == 'female'].Age, color = 'orange', label = 'mulheres', alpha = 0.5, edgecolor = 'black')

plt.legend(loc='upper right')


plt.savefig(r'E:\Users\quadr\Documents\Projetos\PA-Analytics\Python Básico para Data Science e Analytics\Curso\V2.0\Bases\Bonus 1' +  parte_variavel + '.png')


# In[16]:


base.to_excel(r'E:\Users\quadr\Documents\Projetos\PA-Analytics\Python Básico para Data Science e Analytics\Curso\V2.0\Bases\Bonus 1' +  parte_variavel + '_tratada.xlsx')


# In[ ]:




