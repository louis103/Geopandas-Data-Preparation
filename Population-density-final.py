import pandas as pd
import numpy as np
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

#reading the hand made excel file carrying our each county uneployment rates
unemployment_csv = pd.read_csv('unemployment.csv')
# print(unemployment_csv.head())
#now we have to load the shapefile geodataframe
shapefile = gpd.read_file('C:/Users/LOUIS/kenyan-counties/County.shp')
shapefile = shapefile[['COUNTY','geometry']]
shapefile.rename(columns={'COUNTY':'County'},inplace=True)
# print(shapefile)

#now its time to replace the missing county names
shapefile.replace('Keiyo-Marakwet','Elgeyo-Marakwet',inplace=True)
shapefile.replace('Tharaka','Tharaka-Nithi',inplace=True)
# print(shapefile)
# shapefile.to_csv('Complete_edited_kenyan_couties.csv')
#now lets merge the two datasets,shapefile and enemployment_csv
shapefile = shapefile.merge(unemployment_csv,on='County')
# print(shapefile)
shapefile.to_file('unemployment/Unemployment.shp')
print('Successfully created a shapefile')