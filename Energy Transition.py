#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


climate=pd.read_csv("/Users/abhiksengupta/Downloads/ Climate Info.csv")
climate


# In[3]:


climate.columns


# In[4]:


climate.drop("CO2 emissions (kg per 2017 PPP $ of GDP)", axis=1, inplace=True)
climate.drop("Exports of goods and services (% of GDP)", axis=1, inplace=True)
climate.drop("Gross savings (% of GDP)", axis=1, inplace=True)
climate 


# In[5]:


climate.isna().sum()


# In[6]:


climate["Gross fixed capital formation (% of GDP)"].interpolate(method="linear", axis=0, inplace=True)
climate["Trade (% of GDP)"].interpolate(method="linear", axis=0, inplace=True)
climate["Monetary Sector credit to private sector (% GDP)"].interpolate(method="linear", axis=0, inplace=True)


# In[7]:


climate.describe()


# In[8]:


climate["log_CO2"]= np.log(climate['Annual CO_ emissions'])
climate["log_pop"]= np.log(climate['Population, total'])
climate


# In[9]:


import statsmodels.api as sm
import statsmodels.formula.api as smf 
import statsmodels.tools.tools as smt
import statsmodels.stats.diagnostic as smd
from statsmodels.compat import lzip


# In[10]:


climate.columns


# In[11]:


climate.rename(columns={"Population, total":"Population"},inplace= True)
climate.rename(columns={"Renewables (TWh growth - equivalent)":"RE"},inplace= True)
climate.rename(columns={"Foreign direct investment, net inflows (% of GDP)":"FDIInflows"},inplace= True)
climate.rename(columns={"Gross fixed capital formation (% of GDP)":"GFCF"},inplace= True)
climate.rename(columns={"Monetary Sector credit to private sector (% GDP)":"CredittoPvt"},inplace= True)
climate.rename(columns={"GDP, PPP (constant 2017 international $)":"GDP"},inplace= True)
climate.rename(columns={"Total natural resources rents (% of GDP)":"TotalNaturalRents"},inplace= True)
climate.rename(columns={"Domestic credit to private sector by banks (% of GDP)":"DomesticCredit"},inplace= True)
climate.rename(columns={"Human Development Index":"HDI"},inplace= True)
climate.rename(columns={"Annual CO_ emissions":"CO2_ems"},inplace= True)
climate.rename(columns={"Trade (% of GDP)":"Trade"},inplace= True)


# In[12]:


climate.columns


# In[13]:


climate


# In[14]:


mdl=smf.ols('RE~Population+FDIInflows+GFCF+CredittoPvt+Trade+GDP+TotalNaturalRents+DomesticCredit+HDI+CO2_ems+log_CO2+log_pop',data=climate).fit()
mdl.params


# In[15]:


resid=mdl.resid
exog = mdl.model.exog


# In[16]:


bp_test = smd.het_breuschpagan(resid, exog)
print(bp_test)


# In[17]:


alpha = 0.05  
if bp_test[1] < alpha:
    print("Reject null hypothesis of homoskedasticity")
else: 
    print("Fail to reject null hypothesis")


# In[18]:


print(mdl.summary())


# In[19]:


print(mdl.params.index)
print(mdl.pvalues.index)


# In[20]:


climate.groupby('Entity')["TotalNaturalRents"].mean()


# In[21]:


climate.groupby('Entity')["TotalNaturalRents"].hist(alpha=0.3)


# In[22]:


sns.barplot(data=climate, x="Entity", y='GDP')


# In[23]:


from linearmodels.panel import PanelOLS
from linearmodels.panel import compare


# In[24]:


climate.columns


# In[6]:


climate.groupby(SriLanka)[GFCF]


# In[ ]:




