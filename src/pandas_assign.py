import pandas as pd
import numpy as np

students_record = [['Samreena',900],['Mehwish',750],['Asif',895],['Mirha',800],['Affan',850],['Raees',950]]

dataframe = pd.DataFrame(students_record,columns=['Student Names','Student Marks'])
dataframe1 = dataframe.assign(Percentage = lambda x: (x['Student Marks'] / 1000 * 100))
print(dataframe1)
"""
  Student Names  Student Marks  Percentage
0      Samreena            900        90.0
1       Mehwish            750        75.0
2          Asif            895        89.5
3         Mirha            800        80.0
4         Affan            850        85.0
5         Raees            950        95.0
"""
values_list = [['Samreena', 85, 75, 100], ['Mehwish', 90, 75, 90], ['Asif', 95, 82, 80],
               ['Mirha', 75, 88, 68], ['Affan', 80, 63, 70], ['Raees', 91, 64, 90]]

# pandas dataframe creation
df = pd.DataFrame(values_list, columns=['Student Names', 'Computer', 'Math', 'Physics'])

# applying Lambda function

dataframe = df.assign(Marks_Obtained=lambda x: (x['Computer'] + x['Math'] + x['Physics']))

# display dataframe
print(dataframe)

"""
  Student Names  Computer  Math  Physics  Marks_Obtained
0      Samreena        85    75      100             260
1       Mehwish        90    75       90             255
2          Asif        95    82       80             257
3         Mirha        75    88       68             231
4         Affan        80    63       70             213
5         Raees        91    64       90             245

"""