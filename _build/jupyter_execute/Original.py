#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Take-notice!" data-toc-modified-id="Take-notice!-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Take notice!</a></span></li><li><span><a href="#Introduction-to-GIS" data-toc-modified-id="Introduction-to-GIS-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Introduction to GIS</a></span><ul class="toc-item"><li><span><a href="#Data-Types" data-toc-modified-id="Data-Types-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Data Types</a></span></li><li><span><a href="#Spatial-Data-Formats" data-toc-modified-id="Spatial-Data-Formats-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Spatial Data Formats</a></span><ul class="toc-item"><li><span><a href="#Vector-Data" data-toc-modified-id="Vector-Data-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Vector Data</a></span></li><li><span><a href="#Raster-Data" data-toc-modified-id="Raster-Data-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Raster Data</a></span></li></ul></li><li><span><a href="#Introduction-to-GIS-for-the-Social-Sciences" data-toc-modified-id="Introduction-to-GIS-for-the-Social-Sciences-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Introduction to GIS for the Social Sciences</a></span><ul class="toc-item"><li><span><a href="#Geographic-Hierarchy" data-toc-modified-id="Geographic-Hierarchy-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Geographic Hierarchy</a></span></li></ul></li></ul></li><li><span><a href="#Python-and-census-data" data-toc-modified-id="Python-and-census-data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Python and census data</a></span><ul class="toc-item"><li><span><a href="#Where-to-get-census-data?" data-toc-modified-id="Where-to-get-census-data?-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Where to get census data?</a></span></li><li><span><a href="#The-libraries" data-toc-modified-id="The-libraries-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>The libraries</a></span></li><li><span><a href="#Importing-data" data-toc-modified-id="Importing-data-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Importing data</a></span></li><li><span><a href="#Preliminary-inspection" data-toc-modified-id="Preliminary-inspection-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Preliminary inspection</a></span></li><li><span><a href="#Data-types" data-toc-modified-id="Data-types-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Data types</a></span><ul class="toc-item"><li><span><a href="#The-FIPS-code" data-toc-modified-id="The-FIPS-code-3.5.1"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>The FIPS code</a></span></li></ul></li><li><span><a href="#Delete-county-row" data-toc-modified-id="Delete-county-row-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Delete county row</a></span></li><li><span><a href="#The-census-data-dictionary" data-toc-modified-id="The-census-data-dictionary-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>The census data dictionary</a></span></li><li><span><a href="#Dropping-columns" data-toc-modified-id="Dropping-columns-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Dropping columns</a></span></li><li><span><a href="#Renaming-columns" data-toc-modified-id="Renaming-columns-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>Renaming columns</a></span></li><li><span><a href="#Double-check-your-data-integrity" data-toc-modified-id="Double-check-your-data-integrity-3.10"><span class="toc-item-num">3.10&nbsp;&nbsp;</span>Double check your data integrity</a></span></li><li><span><a href="#Simple-stats-and-plots" data-toc-modified-id="Simple-stats-and-plots-3.11"><span class="toc-item-num">3.11&nbsp;&nbsp;</span>Simple stats and plots</a></span></li><li><span><a href="#Create-your-first-plot" data-toc-modified-id="Create-your-first-plot-3.12"><span class="toc-item-num">3.12&nbsp;&nbsp;</span>Create your first plot</a></span></li><li><span><a href="#Sorting" data-toc-modified-id="Sorting-3.13"><span class="toc-item-num">3.13&nbsp;&nbsp;</span>Sorting</a></span></li><li><span><a href="#Filtering-and-subsetting-data" data-toc-modified-id="Filtering-and-subsetting-data-3.14"><span class="toc-item-num">3.14&nbsp;&nbsp;</span>Filtering and subsetting data</a></span></li><li><span><a href="#Totals-are-great-but-let's-normalize-the-data" data-toc-modified-id="Totals-are-great-but-let's-normalize-the-data-3.15"><span class="toc-item-num">3.15&nbsp;&nbsp;</span>Totals are great but let's normalize the data</a></span></li></ul></li><li><span><a href="#Maps!" data-toc-modified-id="Maps!-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Maps!</a></span><ul class="toc-item"><li><span><a href="#Using-subplots-to-create-multiple-plots" data-toc-modified-id="Using-subplots-to-create-multiple-plots-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Using subplots to create multiple plots</a></span></li></ul></li><li><span><a href="#Advanced-topics" data-toc-modified-id="Advanced-topics-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Advanced topics</a></span><ul class="toc-item"><li><span><a href="#Additional-mapping-ideas" data-toc-modified-id="Additional-mapping-ideas-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Additional mapping ideas</a></span></li><li><span><a href="#Add-a-basemap" data-toc-modified-id="Add-a-basemap-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Add a basemap</a></span><ul class="toc-item"><li><span><a href="#Project-to-web-mercator" data-toc-modified-id="Project-to-web-mercator-5.2.1"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>Project to web mercator</a></span></li></ul></li></ul></li></ul></div>

# <div class="alert alert-danger">
# 
# <h1>Take notice!</h1>
# <ul>
#     <li>This class will be recorded</li>
# </ul>
#     
# </div>

# Introduction to GIS
# ===================
# 
# *Special thanks to Albert Kochaphum for sharing some of [his material](https://github.com/albertkun/Introduction_to_GIS_SS_Sp21) for this workshop.*
# 
# What is GIS? Depending on who you ask, GIS has two meanings:
# 
# **Geographic Information System** typically refers to applications and
# software that is used to create spatial data and to investigate spatial
# relationships between that data.
# 
# **Geographic Information Science** is the framework we use to ask questions
# about the spatial relationship between data.

# For example, predicting the effects of climate change (rising
# sea-levels) on low laying areas (elevation) would be an application of
# Geographic Information Science, while the software to do the predictions
# would be an example of a Geographic Information System.
# 
# In short:
# 
# ![](./images/image1.png)

# Data Types
# ----------
# 
# There are two key distinction between data types, spatial or non-spatial
# data.
# 
# Spatial data is data that already contains geographic information.
# 
# Common file types are the following:
# 
# -   **Shapefiles:** `.zip` (these are made up of 3 or more files, and the .shp is
#     commonly used to identify them)
# 
# -   **KML files:** `.kml`, `.kmz`
# 
# -   **GeoJSON files:** `.geojson`
# 
# -   **Image files**: `.jpg`, `.png`, `.tiff`

# Non-spatial data is data that has no geographic information.
# 
# Common non-spatial data are the following:
# 
# -   **Excel Spreadsheets**: `.xlsx`, `.xls`
# 
# -   **Comma/Table Separated Value files**: `.csv`
# 
# -   **JSON files**: `.json`
# 
# -   **dBase database file**: `.dbf`
# 
# When non-spatial data has geographic attributes, like zipcodes,
# addresses, city names, or even latitude/longitude coordinates it can be
# turned into spatial data. The distinction is that non-spatial data will
# only show up as tables in GIS applications.

# On the other hand, spatial data that has data attributes can be turned
# into a non-spatial data type by saving/exporting its data as tables. The
# following graphic summarizes this relationship:
# 
# ![](./images/image2.png)

# Spatial Data Formats
# --------------------
# 
# There are several data spatial data models that you may encounter as you
# work with geo data. Geodata formats are commonly divided into two types,
# vector data or a raster data. In GIS, discrete data means that the data
# has a fixed location. Continuous data in GIS does not have well defined
# or no boundary at all, the most common example is elevation. The graphic
# below shows how vector data and raster data formats can represent
# continuous or discrete data:
# 
# ![alt text](./images/image3.png)
# 
# Spatial Data Types (Source: Michele Tobias, UC Davis)
# 
# The graphic also illustrates how certain vector data is often better
# suited for discrete data, while raster data is often better used for
# continuous data. Let's go into a little more detail about each!

# ### Vector Data
# 
# Vector data represents discrete objects in the real world with points,
# lines, and polygons in the dataset.
# 
# If you were to draw a map to your house for a friend, you would
# typically use vector data - roads would be lines, a shopping center
# included as an important landmark might be a rectangle of sorts, and
# your house might be a point (perhaps represented by a star or a house
# icon).

# ### Raster Data
# 
# Raster data represents continuous fields or discrete objects on a grid,
# storing measurements or category names in each cell of the grid.
# 
# Digital photos are raster data you are already familiar with. If you
# zoom in far enough on a digital photo, you\'ll see that photo is made up
# of pixels, which appear as colored squares. Pixels are cells in a
# regular grid and each contains the digital code that corresponds to the
# color that should be displayed there.
# 
# You may be surprised to see jpgs listed as a data type that you may have
# thought to be non-spatial, but satellite imagery is commonly stored in
# photo formats.

# Introduction to GIS for the Social Sciences
# -------------------------------------------
# 
# Now that we have a good understanding of geospatial data, we can explore
# the GIS connection to the social sciences.
# 
# Geography is divided into physical geography (natural systems) and human
# geography (human-made systems). The social sciences sit within
# human-made systems and the data here is often captured in specific
# units. Such as number of people living in a specific city or the
# language spoken in a country. Most of the data we will encounter
# will be discrete.

# The following election result map shows the number of people from each state that voted for either Biden or Trump in the 2020 general election.
# 
# <img src="images/image2021_1.png" width=800>
# 
# Source: [New York Times,
# 2020](https://www.nytimes.com/interactive/2020/11/03/us/elections/results-president.html)
# 
# The states themselves are the boundaries, even though the data is
# collected at smaller levels.
# 
# How is that possible? 

# ### Geographic Hierarchy
# 
# Move over Aristotle: The **sum** is the whole of its parts!
# 
# The first law of Geography (and perhaps only) is "**everything is
# related to everything else, but nearer things are more related than
# distant things.**" When thinking about human data, there are many
# different units, countries, states, cities, and even households.
# Whenever this data is being summarized to larger geographies, as long as
# the smaller boundaries do not overlap then you can do so. However, this
# does not mean it is always safe to do so, why?

# Keeping the first law of geography in mind, when you summarize smaller
# data to larger geographies (i.e. going from cities to a state), the
# nearer things become less related because they are summarized to a
# larger geographic relation. Let's return to the election map, but
# break it down into counties to see how the summing of the data changed
# spatial relationships.
# 
# <img src="images/image2021_2.png" width=800>
# 
# 
# Source: [USA Today,
# 2020](https://www.usatoday.com/in-depth/graphics/2020/11/10/election-maps-2020-america-county-results-more-voters/6226197002/#mainContentSection)

# How does this map compare to the previous map?
# 
# <img src="images/image2021_1.png" width=800>
# 
# For one thing, you can see that a state like Nevada is not completely blue and has quite a bit of Republican voters. When a whole state is considered “democrat” or blue, such types of simplifications can only occur when data from the counties is summarized upwards to the state level.

# Below is an example of how the United States Census Bureau’s uses hierarchal geography: 
# 
# <img src="images/image6.png">

# # Python and census data
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
# <a href="https://censusreporter.org" target="_blank"><img src="images/cr.png"></a>

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


# # Maps!

# We can now create choropleth maps in geopandas. 
# 
# * [geopandas choropleth maps](https://geopandas.org/mapping.html#choropleth-maps)
# * [color schemes with mapclassify](https://pysal.org/notebooks/viz/mapclassify/intro.html)
# 
#   * `equal_interval`
#   * `quantiles`
#   * `user_defined`
#   * etc...

# In[42]:


gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='equal_interval')


# In[43]:


gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='quantiles')


# In[44]:


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

# In[45]:


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


# # Advanced topics

# ## Additional mapping ideas
# Research question: What does the majority ethnic cluster look like in Los Angeles?
# 
# You can answer this question by using python queries.
# 
# <img src="images/query.png">

# In[46]:


# query the data for where there are more than 80% hispanics
gdf[gdf['Percent Hispanic'] > 80]


# In[47]:


gdf[gdf['Percent Hispanic'] > 90].plot(figsize=(12,10))


# <div class="alert alert-info">
# 
# Now it's your turn! Create map plots based on other race indicators with varying segments of the population.
# 
# </div>

# In[ ]:





# ## Add a basemap
# 
# Adding a basemap to a geopandas plot can be done using the [contextily library](https://contextily.readthedocs.io/en/latest/intro_guide.html). To do so, you must:
# 
# * reproject your geodataframe to Web Mercator (epsg: 3857)
# * add a basemap, use the following [guidelines](https://github.com/geopandas/contextily/blob/master/notebooks/providers_deepdive.ipynb)

# ### Project to web mercator
# 
# ![projections](https://www.esri.com/arcgis-blog/wp-content/uploads/2022/02/grid2.png)
# 
# In order to conduct spatial analysis, it is recommended to use a projected coordinate system, rather than a geographic coordinate system (which uses angular measurements). Here is an [blog post from ESRI](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/gcs_vs_pcs/) that describes the differences between the two.

# In[48]:


# reproject to Web Mercator
gdf_web_mercator = gdf.to_crs(epsg=3857)
gdf_web_mercator


# In[49]:


# use subplots that make it easier to create multiple layered maps
fig, ax = plt.subplots(figsize=(15, 15))

# add the layer with ax=ax in the argument 
gdf_web_mercator[gdf_web_mercator['Percent Hispanic'] > 50].plot(ax=ax, alpha=0.8)

# turn the axis off
ax.axis('off')

# set a title
ax.set_title('Census Tracts with more than 50% Hispanic Population',fontsize=16)

# add a basemap
ctx.add_basemap(ax)


# # Thank you!
# 
# Please take a very quick survey, and let us know your thoughts on the workshop.
# 
# https://forms.gle/nbWgNP45qCwZhLRh9
# 

# In[ ]:




