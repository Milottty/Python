import pandas as pd

data = pd.read_csv('avgIQpercountry.csv')

# print(data)


firt_rows = data.head(10)
print(firt_rows)
last_rows = data.tail(10)
print(last_rows)
