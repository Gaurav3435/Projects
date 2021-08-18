#Gaurav patil A-33
#load library
import pandas as pd
import matplotlib.pyplot as plt  
#load data
df = pd.read_csv("company_sales_data.csv")
monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
#plot
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
#label
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
#show
plt.show()