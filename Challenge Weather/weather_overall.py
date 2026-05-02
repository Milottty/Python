import pandas  as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

print(df.info())

df["full_date"] = pd.to_datetime(
    df['year'].astype(str) + '/' + df["day"],
    format='%Y/%m/%d'
)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
mesatarja = df['temperature'].mean()
print(f"the avg temp is {mesatarja:}  C")