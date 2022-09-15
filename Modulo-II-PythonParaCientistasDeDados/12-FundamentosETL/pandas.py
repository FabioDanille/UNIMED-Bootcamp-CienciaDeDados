import pandas as pd

url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
df1 = pd.read_csv(url)
# Dataset is now stored in a Pandas Dataframe


#############################################


import pandas as pd

url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
# salaries CSV
print(sf.head())

