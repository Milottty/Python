


import pandas as pd

products = ['Apples', 'Bananas', 'Oranges', 'Grapes']

sales = [150, 200, 180, 60]

sales_series = pd.Series(sales, index=products)
print(sales_series)

print(sales_series['Grapes'])

total_sales = sales_series.sum()
print(total_sales)

best_selling = sales_series.idxmax()
print(f"Best selling product:  {best_selling}")

data = {'Name': ['Miloti', 'Diari', 'Marsi'],
        'Age': [17, 15, 16],
        'City': ['Lipjan', 'Prishtin', 'Prishtin']
        }

klasa = pd.DataFrame(data)
print(klasa)

