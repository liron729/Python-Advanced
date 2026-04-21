import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

df.columns = df.columns.str.strip().str.lower()

df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['day'])

df['temperature'] = df['temperature'].astype(str).str.strip().str.replace('(', '').str.replace(')', '')
df['temperature'] = df['temperature'].astype(float)

avg_temp = df['temperature'].mean()
print(f"Average Temperature: {avg_temp:.2f}°C")

df['month'] = df['date'].dt.month

monthly_avg = df.groupby('month')['temperature'].mean()
print("\nMonthly Average Temperature:")
print(monthly_avg)

plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

hottest_day = df.loc[df['temperature'].idxmax()]
coldest_day = df.loc[df['temperature'].idxmin()]

print("\n Hottest Day:")
print(hottest_day)

print("\n Coldest Day:")
print(coldest_day)

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'], marker='o')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['season'] = df['month'].apply(get_season)

seasonal_avg = df.groupby('season')['temperature'].mean()

print("\nSeasonal Average Temperature:")
print(seasonal_avg)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

df.columns = df.columns.str.strip().str.lower()

df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['day'])

df['temperature'] = df['temperature'].astype(str).str.replace('(', '').str.replace(')', '').str.strip().astype(float)
df['humidity'] = df['humidity'].astype(float)
df['atmospheric pressure'] = df['atmospheric pressure'].astype(float)

print("\n BASIC STATS")
print(df[['temperature','humidity','atmospheric pressure']].describe())

print("\n CORRELATION MATRIX")
print(df[['temperature','humidity','atmospheric pressure']].corr())

df['temp_ma7'] = df['temperature'].rolling(window=7).mean()

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'], label="Temperature", alpha=0.5)
plt.plot(df['date'], df['temp_ma7'], label="7-day Moving Avg", color='red')
plt.legend()
plt.title("Temperature Trend")
plt.show()

plt.figure(figsize=(6,5))
plt.scatter(df['temperature'], df['humidity'], alpha=0.5)
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.show()

plt.figure(figsize=(6,5))
plt.scatter(df['temperature'], df['atmospheric pressure'], alpha=0.5, color='green')
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.title("Temperature vs Pressure")
plt.show()

print("\n HOTTEST DAY")
print(df.loc[df['temperature'].idxmax()])

print("\n COLDEST DAY")
print(df.loc[df['temperature'].idxmin()])

print("\n MOST HUMID DAY")
print(df.loc[df['humidity'].idxmax()])

print("\n LEAST HUMID DAY")
print(df.loc[df['humidity'].idxmin()])

df['temp_range'] = df['temperature'] - df['temperature'].min()

plt.figure(figsize=(10,4))
plt.plot(df['date'], df['temp_range'], color='purple')
plt.title("Daily Temperature Range")
plt.show()

df['month'] = df['date'].dt.month

monthly_avg = df.groupby('month')['temperature'].mean()

plt.figure(figsize=(8,4))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Monthly Avg Temperature")
plt.show()

print("\n SUMMARY")
print(f"Average Temperature: {df['temperature'].mean():.2f}")
print(f"Average Humidity: {df['humidity'].mean():.2f}")
print(f"Average Pressure: {df['atmospheric pressure'].mean():.2f}")


def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['season'] = df['date'].dt.month.apply(get_season)

seasonal_temperature = df.groupby('season')['temperature'].mean()

season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
seasonal_temperature = seasonal_temperature.reindex(season_order)