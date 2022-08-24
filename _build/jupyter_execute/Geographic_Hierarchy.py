#!/usr/bin/env python
# coding: utf-8

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
