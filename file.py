# Meixiang and I are practicing merge 

import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
data1 = pd.DataFrame(data)
#print(data1.head())
columns = data1[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]

plt.plot('Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', data=data1)
plt.show()

