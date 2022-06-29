import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4,5],
    'Names':['Samreena','Asif','Mirha','Affan','Mahwish'],
    'Age':[20,25,15,10,30],
    'Monthly Income':[4000,6000,5000,2000,8000]
})
df['Monthly Income']=df.apply(lambda x: x['Monthly Income']+1000,axis=1)
print(df)

"""
   ID     Names  Age  Monthly Income
0   1  Samreena   20            5000
1   2      Asif   25            7000
2   3     Mirha   15            6000
3   4     Affan   10            3000
4   5   Mahwish   30            9000
"""


import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4,5],
    'Names':['Samreena','Asif','Mirha','Affan','Mahwish'],
    'Age':[20,25,15,10,30],
    'Monthly Income':[4000,6000,5000,2000,8000]
})
print(list(filter(lambda x: x<25,df['Age'])))

"""
   ID     Names  Age  Monthly Income
0   1  Samreena   20            5000
1   2      Asif   25            7000
2   3     Mirha   15            6000
3   4     Affan   10            3000
4   5   Mahwish   30            9000
[20, 15, 10]
"""
