import geopandas as gpd
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt


#reading a csv file
pop_data = pd.read_csv('C:/Users/LOUIS/Documents/fake/Population-Counties.csv')

#for population_data in pop_data:
#    print(population_data)


new_data = pop_data[['County','Population Density']]
# print(new_data)

# new_data.to_csv('Filtered_Population_Density.csv')

#reading a shapefile using geopandas

shapefile_data = gpd.read_file('C:/Users/LOUIS/shp/KEN_adm3.shp')
# print(shapefile_data)
# shapefile_data.to_csv('Shapefile_kenya_counties.csv')

# print(shapefile_data.crs) #{'init': 'epsg:4326'}
shapefile_data = shapefile_data[['NAME_2','geometry']]
shapefile_data2 = gpd.read_file('C:/Users/LOUIS/kenyan-counties/County.shp')

# shapefile_data2.to_csv('Counties_shp_columns.csv')
shapefile_data2 = shapefile_data2[['COUNTY','geometry']]
shapefile_data2.rename(columns={'COUNTY':'County'},inplace=True)
shapefile_data2.to_crs(epsg=4326,inplace=True)
# print(shapefile_data2)

#checking for missing counties in both dataframes

#one is Tharaka and Keiyo-Marakwet
shapefile_data2.replace('Keiyo-Marakwet','Elgeyo-Marakwet',inplace=True)
shapefile_data2.replace('Tharaka','Tharaka-Nithi',inplace=True)

# for index, row in shapefile_data2['County'].iteritems():
#     if row in new_data['County'].tolist():
#         pass
#     else:
#         print('The county {', row, '} is not the new data list')
#
# print(new_data)
# print(shapefile_data2)

#create a new population_density in our shapefile2 geo-dataframe
shapefile_data2 = shapefile_data2.merge(new_data,on='County')
shapefile_data2.rename(columns={'Population Density':'Population Density (People/sq.km)'},inplace=True)
# print(shapefile_data2.columns)
print(shapefile_data2)
# shapefile_data2.to_csv('Complete-Kenyan-counties-population-density.csv')
# shapefile_data2.to_file('Complete-Kenyan-counties-population-density.shp')
