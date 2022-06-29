import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4,5],
    'Names':['Samreena','Asif','Mirha','Affan','Mahwish'],
    'Age':[20,25,15,10,30],
    'Monthly Income':[4000,6000,5000,2000,8000]
})
df['Monthly Income']=list(map(lambda x: int(x+x*0.5),df['Monthly Income']))
print(df)
"""
   ID     Names  Age  Monthly Income
0   1  Samreena   20            6000
1   2      Asif   25            9000
2   3     Mirha   15            7500
3   4     Affan   10            3000
4   5   Mahwish   30           12000
"""


import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4,5],
    'Names':['Samreena','Asif','Mirha','Affan','Mahwish'],
    'Age':[20,25,15,10,30],
    'Monthly Income':[4000,6000,5000,2000,8000]
})
df['Category']=df['Monthly Income'].apply(lambda x: 'Stable' if x>=5000 else 'UnStable')
print(df)

"""
   ID     Names  Age  Monthly Income  Category
0   1  Samreena   20            4000  UnStable
1   2      Asif   25            6000    Stable
2   3     Mirha   15            5000    Stable
3   4     Affan   10            2000  UnStable
4   5   Mahwish   30            8000    Stable
"""
