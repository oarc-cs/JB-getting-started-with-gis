#!/usr/bin/env python
# coding: utf-8

# # Maps

# In[1]:


# to read and visualize spatial data
import geopandas as gpd

# to provide basemaps 
import contextily as ctx

# to give more power to your figures (plots)
import matplotlib.pyplot as plt


# In[2]:


# load a data file
# note the relative filepath! where is this file located?
gdf = gpd.read_file('data/acs2019_5yr_B03002_14000US06037534001.geojson')


# We can now create choropleth maps in geopandas. 
# 
# * [geopandas choropleth maps](https://geopandas.org/mapping.html#choropleth-maps)
# * [color schemes with mapclassify](https://pysal.org/notebooks/viz/mapclassify/intro.html)
# 
#   * `equal_interval`
#   * `quantiles`
#   * `user_defined`
#   * etc...

# In[3]:


gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='equal_interval')


# In[ ]:


gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='quantiles')


# In[ ]:


# custom bins requires an extra argument
gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='user_defined',
                 classification_kwds={'bins':[20,40,60,80,100]})


# ## Using subplots to create multiple plots
# 
# It is often useful to generate multiple plots next to each other. To do so, we look at matplotlib's `subplot` command:
# 
# - https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html

# In[ ]:


# create the 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 12))

# name each subplot
ax1, ax2 = axs

# percent hispanic map on the left
gdf.plot(column='Percent Hispanic', 
            cmap='RdYlGn_r', 
            scheme='user_defined',
            classification_kwds={'bins':[20,40,60,80,100]},
            edgecolor='white', 
            linewidth=0., 
            alpha=0.75, 
            ax=ax1, # this assigns the map to the subplot,
            legend=True
           )

ax1.axis("off")
ax1.set_title("Percent Hispanic")

# percent black map on the right
gdf.plot(column='Percent Non Hispanic Black', 
            cmap='RdYlGn_r', 
            scheme='user_defined',
            classification_kwds={'bins':[20,40,60,80,100]},
            edgecolor='white', 
            linewidth=0., 
            alpha=0.75, 
            ax=ax2, # this assigns the map to the subplot
            legend=True
           )

ax2.axis("off")
ax2.set_title("Percent Non Hispanic Black")

