#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


d1=pd.read_excel("/Users/abhiksengupta/Downloads/PD.xlsx")
d1


# In[3]:


d1.isna().sum()


# In[4]:


d1.columns


# In[5]:


d1[" Credit"]=d1[" Credit"].interpolate(method="linear")
d1["GFCF"]=d1["GFCF"].interpolate(method="linear")
d1["Trade "]=d1["Trade "].interpolate(method="linear")


# In[6]:


d1.isna().sum()


# In[14]:


fig, axes=plt.subplots(3, 3, figsize=(15, 10))

sns.set_style(style='white')
sns.lineplot(ax=axes[0,0], data=d1, x='year', y='REG', hue='country')
axes[0,0].legend(bbox_to_anchor=(0, 1), loc=2)
axes[0,0].set_title('Renewable energy', fontdict= { 'fontsize': 14, 'fontweight':'bold'})
axes[0,0].set(ylabel=None)
sns.lineplot(ax=axes[0,1], data=d1, x='year', y='Trade ', hue='country')
axes[0,1].set(ylabel=None)
axes[0,1].set_title('Trade',fontdict= { 'fontsize': 14, 'fontweight':'bold'})
axes[0,1].get_legend().set_visible(False)
sns.lineplot(ax=axes[0,2], data=d1, x='year', y=' Credit', hue='country')
axes[0,2].set(ylabel=None)
axes[0,2].set_title('Domestic Credit',fontdict= {'fontsize': 14, 'fontweight':'bold'})
axes[0,2].get_legend().set_visible(False)
sns.lineplot(ax=axes[1,0], data=d1, x='year', y='Natural Rents', hue='country')
axes[1,0].set(ylabel=None)
axes[1,0].set_title('Natural Rents',fontdict= { 'fontsize': 14, 'fontweight':'bold'})
axes[1,0].get_legend().set_visible(False)
sns.lineplot(ax=axes[1,1], data=d1, x='year', y='GFCF', hue='country')
axes[1,1].set(ylabel=None)
axes[1,1].set_title('Gross fixed capital formation (% of GDP)',fontdict= {'fontsize': 14, 'fontweight':'bold'})
axes[1,1].get_legend().set_visible(False)
fig.delaxes(axes[2,2])
fig.delaxes(axes[2,1])
fig.delaxes(axes[2,0])
fig.delaxes(axes[1,2])
plt.tight_layout()

plt.show()


# In[15]:


from scipy.stats import pearsonr


# In[19]:


d2=d1[['Trade ', 'Natural Rents', 'GFCF', ' Credit', 'REG']]
d2


# In[23]:


corr_matrix = d2.corr()
p_values = np.zeros_like(corr_matrix)

for i in range(d2.shape[1]):
    for j in range(d2.shape[1]):
        if i == j:
            p_values[i, j] = np.nan
        else:
            corr, p_value = pearsonr(d2.iloc[:, i], d2.iloc[:, j])
            corr_matrix.iloc[i, j] = corr
            p_values[i, j] = p_value
            
            
plt.figure(figsize=(10, 8))
ax=sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0, vmin=-1, vmax=1)


for i in range(corr_matrix.shape[0]):
    for j in range(corr_matrix.shape[1]):
        if i != j:
            p_value = p_values[i, j]
            if p_value < 0.05:
                ax.text(j + 0.5, i + 0.5, "*", ha="center", va="center", color="black", fontsize=12)
plt.title("Correlation Matrix")
plt.show()


# In[38]:


import plotly.graph_objects as go
ren=d1.groupby("year")["REG"].sum().reset_index()
credit=d1.groupby("year")[" Credit"].sum().reset_index()
fig=go.Figure()
fig.add_trace(
   go.Scatter(x=ren["year"], y=ren["REG"], name="Renewable Energy")

)
fig.add_trace(
   go.Scatter(x=credit["year"], y= credit[" Credit"], name="Domestic Credit")

)

fig.update_layout(
    title='Relationship between Renewable Energy and Domestic Credit',
    xaxis_title='year',
    yaxis_title=None,
    legend_title=None,showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=d1['year'], tickangle=90)
    
)

fig.show()


# In[37]:


import plotly.graph_objects as go
ren=d1.groupby("year")["REG"].sum().reset_index()
GF=d1.groupby("year")["GFCF"].sum().reset_index()
fig=go.Figure()
fig.add_trace(
   go.Scatter(x=ren["year"], y=ren["REG"], name="Renewable Energy")

)
fig.add_trace(
   go.Scatter(x=GF["year"], y= GF["GFCF"], name="Gross Fixed Capital Formation")

)

fig.update_layout(
    title='Relationship between Renewable Energy and Gross Fixed Capital Formation',
    xaxis_title='year',
    yaxis_title=None,
    legend_title=None,showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=d1['year'], tickangle=90)
    
)

fig.show()


# In[33]:


d1.columns


# In[36]:


import plotly.graph_objects as go
ren=d1.groupby("year")["REG"].sum().reset_index()
Tr=d1.groupby("year")["Trade "].sum().reset_index()
fig=go.Figure()
fig.add_trace(
   go.Scatter(x=ren["year"], y=ren["REG"], name="Renewable Energy")

)
fig.add_trace(
   go.Scatter(x=Tr["year"], y= Tr["Trade "], name="Trade")

)

fig.update_layout(
    title='Relationship between Renewable Energy and Trade',
    xaxis_title='year',
    yaxis_title=None,
    legend_title=None,showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=d1['year'], tickangle=90)
    
)

fig.show()


# In[35]:


import plotly.graph_objects as go
ren=d1.groupby("year")["REG"].sum().reset_index()
NR=d1.groupby("year")["Natural Rents"].sum().reset_index()
fig=go.Figure()
fig.add_trace(
   go.Scatter(x=ren["year"], y=ren["REG"], name="Renewable Energy")

)
fig.add_trace(
   go.Scatter(x= NR["year"], y= NR["Natural Rents"], name="Total Natural Resource Rent")

)

fig.update_layout(
    title='Relationship between Renewable Energy and Total Natural Resource Rent',
    xaxis_title='year',
    yaxis_title=None,
    legend_title=None,showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=d1['year'], tickangle=90)
    
)

fig.show()


# In[39]:


data = pd.DataFrame(np.random.normal(size=100000))

data.plot(kind="density",
              figsize=(10,10));


plt.vlines(data.mean(),     # Plot black line at mean
          ymin=0, 
          ymax=0.4,
         linewidth=5.0);

plt.vlines(data.median(),   # Plot red line at median
           ymin=0, 
           ymax=0.4, 
           linewidth=2.0,
           color="red");


# In[ ]:




