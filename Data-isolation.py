import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#initialize our default directory
WORKING_DIR = "C:/Users/LOUIS/new"

#opening our excel file
excel_data = pd.read_csv(WORKING_DIR+"/Subcounties_updated2.csv")
# print(excel_data.columns)
#
subcounties_shp = gpd.read_file("C:/Users/LOUIS/new/subcounty/ken_admbnda_adm2_iebc_20191031.shp")
# print(subcounties_shp)

#filtering our needed column data
excel_data = excel_data[['County_name','County_code','Subcounty_name','Subcounty_code',
                         'Longitudes','Latitudes','population','Unemployment_rate','Crime_count_per_month']]
# subcounties_shp.to_csv('subcounties.csv')
subcounties_shp = subcounties_shp[['ADM1_EN','ADM2_EN']]
# print(subcounties_shp)

#rename columns
subcounties_shp.rename(columns={'ADM1_EN':'County_name','ADM2_EN':'Subcounty_name'},inplace=True)
# print(subcounties_shp)
#We merge the two dataframes on the County_name column
subcounties_shp = subcounties_shp.merge(excel_data,on='County_name')
# print(subcounties_shp)
#we convert our merged dataframes into one csv file
subcounties_shp.to_csv('POINTS/Merged_points_Data_Subcounties.csv')
subcounties_shp.to_file('POINTS/Merged_points_Data_Subcounties.shp')
print('Created files successfully')