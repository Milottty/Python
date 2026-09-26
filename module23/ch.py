import streamlit as st
import pandas as pd
import plotly.express as px


weather_df = pd.read_csv("weather.csv")

st.title("Monthly Weather Analysis")
st.write("This app analyzes the average monthly temperature.")



month_order = [
    "Janar",
    "Shkurt",
    "Mars",
    "Prill",
    "Maj",
    "Qershor",
    "Korrik",
    "Gusht",
    "Shtator",
    "Tetor",
    "Nentor",
    "Dhjetor"
]



monthly_average = (
    weather_df
    .groupby(["month", "year"])["temperature"]
    .mean()
    .reset_index()
)

monthly_average = monthly_average.rename(
    columns={"temperature": "Average Temperature (°C)"}
)



monthly_average["month"] = pd.Categorical(
    monthly_average["month"],
    categories=month_order,
    ordered=True
)


monthly_average = monthly_average.sort_values("month")


st.subheader("Summary Statistics")

total_months = monthly_average.shape[0]

average_temperature = monthly_average["Average Temperature (°C)"].mean()


col1, col2 = st.columns(2)

col1.metric("Total Months", total_months)

col2.metric(
    "Average Temperature",
    f"{average_temperature:.2f} °C"
)


st.subheader("Dataset Preview")

st.write(monthly_average)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Temperature by Month")

    temperature = monthly_average.set_index("month")[
        "Average Temperature (°C)"
    ]

    st.bar_chart(temperature)


with col2:
    st.subheader("Temperature Trend")
    st.line_chart(temperature)


max_temperature = weather_df["temperature"].max()
min_temperature = weather_df["temperature"].min()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Months", total_months)

col2.metric(
    "Average Temperature",
    f"{average_temperature:.2f} °C"
)

col3.metric(
    "Maximum Temperature",
    f"{max_temperature} °C"
)

col4.metric(
    "Minimum Temperature",
    f"{min_temperature} °C"
)

hottest_day = (
    weather_df
    .sort_values("temperature", ascending=False)
    .head(5)
)

coldest_day = (
    weather_df
    .sort_values("temperature", ascending=True)
    .head(5)
)

st.subheader("5 Hottest Days")

st.write(hottest_day)


st.subheader("5 Coldest Days")

st.write(coldest_day)