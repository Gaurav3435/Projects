# Import pandas package 
import pandas as pd 
    
# Define a dictionary containing employee data 
data = {'Name': ['Gaurav', 'Rohit', 'krishna', 'Kishan', 'Mohan'], 
        'Age': [20, 20, 19, 21, 20], 
        'City': ['Amalner', 'Dhule', 'Amalner', 'Pune', 'Bihar']}
    
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 
    
# iloc[row slicing, column slicing] 
print(df.iloc [0:2, 1:3] )