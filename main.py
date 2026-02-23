import sys

import pandas as pd
from datetime import datetime
import os

file_name = "garden_logs.xlsx"
# making a file

new_data = {
     "Soil Moisture": [datetime.now()],
     "Temperature": [26.1],
     "Humidity": [38],
     "Pump Status": ["ON"]
 }
# setting the dataframe

df_new = pd.DataFrame(new_data)
# adding the new_data into the panda dataframe

'''if the file exists:
    1. write it into the xlsx file 
    2. if not create a new file'''

if os.path.exists(file_name):
    df_existing = pd.read_excel(file_name)
    df_combined = pd.concat([df_existing,df_new], ignore_index=True)
else:
    df_combined = df_new


df_combined.to_excel(file_name,index=False)

print("Data appended successfully")
