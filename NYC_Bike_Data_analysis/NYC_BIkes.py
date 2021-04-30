#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")
data.head()


# <b>Data Pre-Processing</b>

# In[3]:


#created new month colum form date
mon=[]
for i in range(len(data['Date'])):
    mon.append(data["Date"][i].split("-")[1])
data['Month']=mon
data.head()


# In[4]:


#update data column
dt=[]
for i in range(len(data['Date'])):
    dt.append(int(data["Date"][i].split("-")[0]))
data['Date']=dt
data.head()


# In[5]:


data.describe()


# from the above anaysis only three column are of int data type

# In[6]:


print("\nUnique values in Precipitation columns")
print(data['Precipitation'].unique())
print("\nRelacing 0.47(s) with 0.47 & t with 0 and converting column into float data type")
data['Precipitation']=data['Precipitation'].replace('0.47 (S)',"0.47")
data['Precipitation']=data['Precipitation'].replace('T',"0")
data['Precipitation']=data['Precipitation'].astype("float")
print("\nTHe data tye of Precipitation is:",data['Precipitation'].dtypes)


# In[7]:


def remove_comma(col):
    results=[]
    for i in range(len(col)):
        if len(col[i].split(","))==2:
            results.append(col[i].split(",")[0]+col[i].split(",")[1])
        else:
            results.append(col[i])
    return results


# In[8]:


print("\nUnique values in Brooklyn Bridge columns")
print(data['Brooklyn Bridge'].unique())
print("\nConverting column into int data type")
data['Brooklyn Bridge']=remove_comma(data['Brooklyn Bridge'])
print("\nAfter Pre-Processing: ")
print(data['Brooklyn Bridge'])
data['Brooklyn Bridge']=data['Brooklyn Bridge'].astype("int")
print("\nTHe data tye of Brooklyn Bridge is:",data['Brooklyn Bridge'].dtypes)


# In[9]:


print("\nUnique values in Manhattan Bridge columns")
print(data['Manhattan Bridge'].unique())
print("\nConverting column into int data type")
data['Manhattan Bridge']=remove_comma(data['Manhattan Bridge'])
print("\nAfter Pre-Processing: ")
print(data['Manhattan Bridge'])
data['Manhattan Bridge']=data['Manhattan Bridge'].astype("int")
print("\nTHe data tye of Manhattan Bridge is:",data['Manhattan Bridge'].dtypes)


# In[10]:


print("\nUnique values in Williamsburg Bridge columns")
print(data['Williamsburg Bridge'].unique())
print("\nConverting column into int data type")
data['Williamsburg Bridge']=remove_comma(data['Williamsburg Bridge'])
print("\nAfter Pre-Processing: ")
print(data['Williamsburg Bridge'])
data['Williamsburg Bridge']=data['Williamsburg Bridge'].astype("int")
print("\nTHe data tye of Williamsburg Bridge is:",data['Williamsburg Bridge'].dtypes)


# In[11]:


print("\nUnique values in Queensboro Bridge columns")
print(data['Queensboro Bridge'].unique())
print("\nConverting column into int data type")
data['Queensboro Bridge']=remove_comma(data['Queensboro Bridge'])
print("\nAfter Pre-Processing: ")
print(data['Queensboro Bridge'])
data['Queensboro Bridge']=data['Queensboro Bridge'].astype("int")
print("\nTHe data tye of Queensboro Bridge is:",data['Queensboro Bridge'].dtypes)


# In[12]:


print("\nUnique values in Total columns")
print(data['Total'].unique())
print("\nConverting column into int data type")
data['Total']=remove_comma(data['Total'])
print("\nAfter Pre-Processing: ")
print(data['Total'])
data['Total']=data['Total'].astype("int")
print("\nTHe data tye of Total is:",data['Total'].dtypes)


# <b>1. Installing Sensors</b>

# In[13]:


print("Comparision of Total Bike movement vs the  Brooklyn Bridge")
data.plot(x="Total", y=["Brooklyn Bridge"], linestyle='dashed')
plt.show()


# In[14]:


print("Comparision of Total Bike movement vs the  Manhattan Bridge")
data.plot(x="Total", y=["Manhattan Bridge"], linestyle='dashed')
plt.show()


# In[15]:


print("Comparision of Total Bike movement vs the  Williamsburg Bridge")
data.plot(x="Total", y=["Williamsburg Bridge"], linestyle='dashed')
plt.show()


# In[16]:


print("Comparision of Total Bike movement vs the  Queensboro Bridge")
data.plot(x="Total", y=["Queensboro Bridge"], linestyle='dashed')
plt.show()


# In[17]:


for mth in data['Month'].unique():
    print("Comparative Graph of all this three brigde vs Total bike movement in month {}".format(mth))
    total=[]
    Brooklyn=[]
    Manhattan=[]
    Williamsburg=[]
    Queensboro=[]
    for i in range(len(data['Month'])):
        if data['Month'][i]==mth:
            total.append(data['Total'][data.index[i]])
            Brooklyn.append(data['Brooklyn Bridge'][data.index[i]])
            Manhattan.append(data['Manhattan Bridge'][data.index[i]])
            Williamsburg.append(data['Williamsburg Bridge'][data.index[i]])
            Queensboro.append(data['Queensboro Bridge'][data.index[i]])
    plt.plot(total,Brooklyn, linestyle='dashed')
    plt.plot(total,Manhattan, linestyle='dashed')
    plt.plot(total,Williamsburg, linestyle='dashed')
    plt.plot(total,Queensboro, linestyle='dashed')
    plt.xticks(rotation=90)
    plt.show()


# In[18]:


print("Comparative Graph of all this three brigde vs Total bike movement in month {}".format(data['Month'].unique()))
data.plot(x="Total", y=["Brooklyn Bridge", "Manhattan Bridge", "Williamsburg Bridge",'Queensboro Bridge'], linestyle='dashed')
plt.show()
print("Total bike passed through 7 month in Brooklyn: ",sum(list(data['Brooklyn Bridge'])))
print("Total bike passed through 7 month in Manhattan: ",sum(list(data['Manhattan Bridge'])))
print("Total bike passed through 7 month in Williamsburg: ",sum(list(data['Williamsburg Bridge'])))
print("Total bike passed through 7 month in Queensboro: ",sum(list(data['Queensboro Bridge'])))


# In[19]:


activities = ['Williamsburg', 'Manhattan', 'Queensboro', 'Brooklyn']
slices = [1318427, 1081178, 920355, 648570]
colors = ['r', 'y', 'g', 'b']
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 2.8, autopct = '%1.1f%%')
plt.legend()
plt.show()


# <b>Total bike passing through the bridges can be arranged in decreasing order as:</b><br> 
# 1.Total bike passed through 7 month in Williamsburg: 1318427<br> 
# 2.Total bike passed through 7 month in Manhattan:    1081178<br> 
# 3.Total bike passed through 7 month in Queensboro:   920355<br> 
# 4.Total bike passed through 7 month in Brooklyn:     648570<br> 

# <b>thus the Sensor can be installed on thsis three bridges:</b><br>
# 1. Williamsburg Bridge<br>
# 2. Manhattan Bridge<br>
# 3. Queensboro Bridge<br>
# Since this three bridge are responsible for most of the bike traffic , this can be used to install sensor 

# <b>2. Deployment of Police officer</b>

# In[20]:


data.head()


# In[21]:


data.plot(x="Total", y=["High Temp (°F)","Low Temp (°F)","Precipitation"], linestyle='dotted')
plt.show()


# Thus we can draw conclusion as:<br>
# When the temperature is low (below 70) ,bike traffic is low<br>
# when the temperature is median(between range 70 to 100 ), bike traffic is high<br>

# Thus<br>
# <b>Next Day Weather forcast can be used to predict the number of bicyclists on that day</b><br>
# Accordingly police officer can be deployed<br>

# <b>3. Prediction of Rainy Day baed on Bicyclist</b>

# In[22]:


T=list(data['Total'])
T.sort()
P=list(data['Precipitation'])
P.sort()
print(T[0],T[-1],T[80])


# In[23]:


plt.plot(T,P)
plt.xticks(rotation=90)
plt.xticks(ticks=None, labels=None)
plt.show()


# As the Precipitation increase the Number of Bicyclist Increase <br>
# THus we can use this for prediction the rainfall<br>
# As the Bicyclist increase the rainfall chances increases<br>
# As the Bicyclist Decreases the rainfall chances Decresase<br>

# In[ ]:




