import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

#reading a shapefile
shapefile = gpd.read_file('C:/Users/LOUIS/SHAPEFILE/Buildings.shp')
print(shapefile.crs)
#changing shapefile crs using geopandas library
shapefile.to_crs(epsg='4326')
print('Changed CRS')
print(shapefile.crs)
shapefile.to_file('C:/Users/LOUIS/SHAPEFILE/Buildings_Updated.shp')