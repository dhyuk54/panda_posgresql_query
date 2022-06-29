import pandas as pd
import numpy as np

students_record = [['Samreena',900],['Mehwish',750],['Asif',895],['Mirha',800],['Affan',850],['Raees',950]]

dataframe = pd.DataFrame(students_record,columns=['Student Names','Student Marks'])
dataframe1 = dataframe.assign(Percentage = lambda x: (x['Student Marks'] / 1000 * 100))
print(dataframe1)