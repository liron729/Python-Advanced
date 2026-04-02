import pandas as pd

data  = {'name':['Egzon', 'Liron', 'Melina'],
         'Age' : [17,18,19],
         'City': ['fushe kosove', 'Presheve', 'Prishtine']}
df = pd.DataFrame(data)
print(df)