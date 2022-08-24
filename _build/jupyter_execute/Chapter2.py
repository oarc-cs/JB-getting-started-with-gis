#!/usr/bin/env python
# coding: utf-8

# # Python and Census Data
# Overview for this workshop:
# 
# - how and where to find and download census data
# - use `geopandas` library to read a geojson file ([documentation](https://geopandas.org/gallery/index.html))
# - use `contextily` to add basemaps ([documentation](https://contextily.readthedocs.io/en/latest/intro_guide.html))
# - renaming columns
# - normalizing data columns
# - simple stats
# - adding basemaps

# ## Where to get census data?
# 
# 
# Well, you have many options, including, getting it directly from the source, the [census bureau website](https://www.census.gov/data.html) itself. We also have, as part of the academic community, a great resource: [Social Explorer](https://www.socialexplorer.com/). With a campus-wide license to have full access to their website, you can download any census variable, that pretty much existed... ever. And, with its easy-to-use user interface, this is a wonderful one-stop shop for your census needs.
# 
# But for data scientists, I recommend another source: [censusreporter.org](https://censusreporter.org/)
# 
# ![](./images/cr.png)

# ## The libraries

# In[1]:


# to read and visualize spatial data
import geopandas as gpd

# to provide basemaps 
import contextily as ctx

# to give more power to your figures (plots)
import matplotlib.pyplot as plt


# ## Importing data
# 
# In order to work with data in python, we need a library that will let us handle "spatial data exploration." We looked at shapefiles with geopandas last week, and for this lab, we will use it to read and wrangle a [geojson](https://en.wikipedia.org/wiki/GeoJSON) file.
# 
# Before we continue, let's make a brief detour and find out how geojson files are constructed:
# 
# - [geojson.io](http://geojson.io/#map=2/20.0/0.0)
# 
# ![geojson](images/geojson.png)

# We make the call to load and read the data that was downloaded from census reporter. Take note at the relative path reference to find the file in your file directory.

# In[2]:


# load a data file
# note the relative filepath! where is this file located?
gdf = gpd.read_file('data/acs2019_5yr_B03002_14000US06037534001.geojson')


# ## Preliminary inspection
# A quick look at the size of the data.

# In[3]:


# get number of rows, columns
gdf.shape


# In[4]:


# get first 5 rows
gdf.head()


# In[5]:


# get a random row
gdf.sample()


# In[6]:


# plot it!
gdf.plot(figsize=(10,10))


# In[7]:


# plot a random row
gdf.sample().plot()


# ## Data types
# 
# To get the data types, we will use `.info()`. 

# In[8]:


# look at columns, null values, and the data types
gdf.info()


# ### The FIPS code
# What is the geoid? It is called a FIPS code but why is it important?
# 
# - https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html
# 
# ![fips](images/fips.png)

# In[9]:


# get first five geoid's
gdf.geoid.head()


# ![fips code](https://learn.arcgis.com/en/related-concepts/GUID-D7AA4FD1-E7FE-49D7-9D11-07915C9ACC68-web.png)
# 
# [Source: ESRI](https://learn.arcgis.com/en/related-concepts/united-states-census-geography.htm)

# ## Delete county row
# 
# As we have observed, the first row in the data obtained from censusreporter is for the entire county. Keeping this row is problematic, as it represents a data record that is at a different scale. Let's delete it.

# <div class="alert alert-danger">
#     <b>Important!</b><hr>
#     Note that any data downloaded from censusreporter will have a "summary row" for the entire data.
# </div>

# In[10]:


# check the data again
gdf.head()


# In[11]:


# drop the row with index 0 (i.e. the first row)
gdf = gdf.drop([0])


# In[12]:


# check to see if it has been deleted
gdf.head()


# ## The census data dictionary
# There are a lot of columns. What are these columns? Column headers are defined in the `metadata.json` file that comes in the dowloaded zipfile from censusreporter. Click the link below to open the json file in another tab.
# 
# * [metadata.json](data/metadata.json)

# Let's identify which columns are needed, and which are not for our exploration.
# 
# ![census variables](images/census1.png)

# ## Dropping columns 
# There are many columns that we do not need. 
# 
# - output existing columns as a list
# - create a list of columns to keep
# - redefine `gdf` with only the columns to keep
# 

# In[13]:


list(gdf) # this is the same as df.columns.to_list()


# In[14]:


# create a list of columns to keep
columns_to_keep = ['geoid',
 'name',
 'B03002001',
 'B03002002',
 'B03002003',
 'B03002004',
 'B03002005',
 'B03002006',
 'B03002007',
 'B03002008',
 'B03002009',
 'B03002012',
 'geometry']


# In[15]:


# redefine gdf with only columns to keep
gdf = gdf[columns_to_keep]


# In[16]:


# check the slimmed down gdf
gdf.head()


# ## Renaming columns
# 
# Let's rename the columns. First, create a list of column names as they are now.

# In[17]:


list(gdf) # this is the same as df.columns.to_list()


# Then, simply copy and paste the output list above, and define the columns with it. Replace the values with your desired column names

# In[18]:


gdf.columns = ['geoid',
 'name',
 'Total',
 'Non Hispanic',
 'Non Hispanic White',
 'Non Hispanic Black',
 'Non Hispanic American Indian and Alaska Native',
 'Non Hispanic Asian',
 'Non Hispanic Native Hawaiian and Other Pacific Islander',
 'Non Hispanic Some other race',
 'Non Hispanic Two or more races',
 'Hispanic',
 'geometry']


# In[19]:


# check the renamed columns
gdf.head()


# ## Double check your data integrity
# Does the math add up? Let's check. The `Total` should equal the rest of the columns.

# In[20]:


# get a random record
random_tract = gdf.sample()
random_tract


# To get values from individual cells in a dataframe, use the `iloc` command.
# 
# - `iloc` ([documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html))
# 
# While there are various methods to get cell values in python, the iloc command allows you to get to a cell based on the position of the record row and the column name.

# In[21]:


# example usage of iloc to get the total population of our random record
# "for the 0th record, get the value in the Total column"
random_tract.iloc[0]['Total']


# In[22]:


# print this out in plain english
print('Total population: ' + str(random_tract.iloc[0]['Total']))


# In[23]:


# non hispanic plus hispanic should equal to the total
print('Non Hispanic + Hispanic: ' + str(random_tract.iloc[0]['Non Hispanic'] + random_tract.iloc[0]['Hispanic']))


# In[24]:


# hispanic plus all the non hispanice categories
print(random_tract.iloc[0]['Non Hispanic White'] + 
      random_tract.iloc[0]['Non Hispanic Black'] + 
      random_tract.iloc[0]['Non Hispanic American Indian and Alaska Native'] + 
      random_tract.iloc[0]['Non Hispanic Asian'] + 
      random_tract.iloc[0]['Non Hispanic Native Hawaiian and Other Pacific Islander'] + 
      random_tract.iloc[0]['Non Hispanic Some other race'] + 
      random_tract.iloc[0]['Non Hispanic Two or more races'] + 
      random_tract.iloc[0]['Hispanic'])


# ## Simple stats and plots

# In[25]:


# access a single column like df['col_name']
gdf['Total'].head()


# In[26]:


# What is the mean?
gdf['Total'].mean()


# In[27]:


# What is the median?
gdf['Total'].median()


# In[28]:


# get some stats
gdf['Total'].describe()


# ## Create your first plot
# 
# - https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

# In[29]:


# plot it as a historgram with 50 bins
gdf['Total'].plot.hist()


# In[30]:


# make it bigger, increase the number of bins, and give it a title
gdf['Total'].plot.hist(figsize=(12,5),
                       bins=100,
                       title='Los Angeles County census tracts by population size (ACS 2019 5-year)')


# <div class="alert alert-info">
#     Now it's your turn. Find some stats for different fields in the data and output them below.
#     </div>

# In[ ]:





# ## Sorting
# What are the top 10 most populated census tracts? What are the census tracts with the highest black popluation? To answer these questions, the simplest method is to sort the data by their respective columns.
# 
# - [pandas sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)

# In[31]:


gdf_sorted = gdf.sort_values(by='Total',ascending = False)


# In[32]:


# display the data, but just a few columns to keep it clean
gdf_sorted[['geoid','Total']].head(10)


# In[33]:


# plot the top 10 most populated tracts
gdf_sorted.head(10).plot(figsize=(10,10))


# In[34]:


# Make it 100 and prettier
gdf_sorted.head(1000).plot(figsize=(10,10),
                          column='Total', 
                          cmap='plasma', 
                          legend=True)


# <div class="alert alert-info">
# Now it's your turn! Create a table and accompanying bar plot for the top/bottom x values for column of your choice.
# </div>

# In[ ]:





# ## Filtering and subsetting data
# Sorting is one method, but the process of discovery compels us to interrogate the data in different ways. One method of doing so is to query, or filter the data to see specific views of the data based on a question you may have. For example, what are the census tract that have no people in them? Or, Which census tracts are more than 75% black?

# In[35]:


# subset the data so that we can see the data per row... 
# in other words, this syntax is asking to "show me the values in my dataframe that match this filter
gdf[gdf['Total']==0]


# Note that unless you specify the resulting output as a new variable, the results are only temporary (in memory). If you want to use the results for subsequent analysis, you need to create a new variable.

# In[36]:


# create a new variable for census tracts with zero pop
gdf_no_pop = gdf[gdf['Total']==0]


# In[37]:


# how many records?
print('There are ' + str(len(gdf_no_pop)) + ' census tracts with no people in them')


# In[38]:


# display it
gdf_no_pop[['geoid','Total']]


# ## Totals are great but let's normalize the data
# 
# For almost any data inquiry, you should ask the question: should I normalize the data? With raw numbers, is it fair to compare one census tract to another? For example, if one census tract has 1000 hispanics, and another has 100, can we assume that the first tract is largely Hispanic? No, because the total population might be 10000 people, resulting in it being 10% hispanic, whereas the second tract might have 200 people living in it, resulting in it being 50% hispanic.

# To avoid these types of misrepresentations, we can normalize the data, and provide it as a percent of total.

# In[39]:


# output columns
list(gdf)


# In[40]:


# create a new column, and populate it with normalized data to get the percent of total value
gdf['Percent Non Hispanic'] = gdf['Non Hispanic']/gdf['Total']*100
gdf['Percent Hispanic'] = gdf['Hispanic']/gdf['Total']*100
gdf['Percent Non Hispanic White'] = gdf['Non Hispanic White']/gdf['Total']*100
gdf['Percent Non Hispanic Black'] = gdf['Non Hispanic Black']/gdf['Total']*100
gdf['Percent Non Hispanic American Indian and Alaska Native'] = gdf['Non Hispanic American Indian and Alaska Native']/gdf['Total']*100
gdf['Percent Non Hispanic Asian'] = gdf['Non Hispanic Asian']/gdf['Total']*100
gdf['Percent Non Hispanic Native Hawaiian and Other Pacific Islander'] = gdf['Non Hispanic Native Hawaiian and Other Pacific Islander']/gdf['Total']*100
gdf['Percent Non Hispanic Some other race'] = gdf['Non Hispanic Some other race']/gdf['Total']*100
gdf['Percent Non Hispanic Two or more races'] = gdf['Non Hispanic Two or more races']/gdf['Total']*100


# In[41]:


# check your work
gdf.sample(5)

