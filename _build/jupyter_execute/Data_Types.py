#!/usr/bin/env python
# coding: utf-8

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
