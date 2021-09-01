#Gaurav patil A-33
#Import necessary library
import pandas as pd
#creating datframe
initial_data = {'Name': ['Gaurav', 'Rohit', 'krishna', 'Kishan', 'Mohan'], 
        'Age': [20, 20, 19, 21, 20], 
        'City': ['Amalner', 'Dhule', 'Amalner', 'Pune', 'Bihar']}
df = pd.DataFrame(initial_data, columns = ['Name','Age', 'City'])
# Create new column using dictionary
new_data = { "Gaurav":"B.Tech",
             "Rohit":"B.Tech",
             "krishna":"MBBS",
             "Kishan":"Diploma",
             "Mohan":"MBBS" }
# combine this new data with existing DataFrame
print("Existing Dataframe:")
df["Qualification"] = df["Name"].map(new_data)
print(df)
#drop column City and Age
print("new Dataframe:")
print(df.drop(['Age','City'], axis = 1))