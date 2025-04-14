
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('covid_19_data.csv')
print("Initial data:")
print(df.head())

# Rename columns
df.rename(columns={
    'Country/Region': 'Country',
    'ObservationDate': 'Date',
    'Confirmed': 'Cases',
    'Deaths': 'Deaths',
    'Recovered': 'Recovered'
}, inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Drop missing values
df.dropna(subset=['Country', 'Cases', 'Deaths', 'Recovered'], inplace=True)

# Country-wise summary
country_summary = df.groupby('Country')[['Cases', 'Deaths', 'Recovered']].sum().sort_values(by='Cases', ascending=False)
print("Top 10 countries by cases:")
print(country_summary.head(10))

# India time series
india_data = df[df['Country'] == 'India']
india_daily = india_data.groupby('Date')[['Cases', 'Deaths', 'Recovered']].sum()
india_daily.plot(title='COVID-19 Trend in India', figsize=(10,5))
plt.xlabel("Date")
plt.ylabel("Count")
plt.grid(True)
plt.show()
