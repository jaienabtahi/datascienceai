import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_parquet("yellow_tripdata_2023-01.parquet")
df2 = pd.read_csv("taxi_zone_lookup.csv")

# Merging data based on location
df1 = df1.merge(df2, left_on='PULocationID', right_on='LocationID', suffixes=('_PU', '_DO'))
df1 = df1.merge(df2, left_on='DOLocationID', right_on='LocationID', suffixes=('_PU', '_DO'))

# Airports zone names
airports = ['JFK Airport', 'LaGuardia Airport', 'Newark Airport']
df1_airports = df1[(df1['Zone_PU'].isin(airports)) | (df1['Zone_DO'].isin(airports))]

# How many pickups happened at each airport?
pickups_at_airports = df1[df1['Zone_PU'].isin(airports)]['Zone_PU'].value_counts()
print("Pickups at airports:\n", pickups_at_airports)

# How many dropoffs happened at each airport?
dropoffs_at_airports = df1[df1['Zone_DO'].isin(airports)]['Zone_DO'].value_counts()
print("Dropoffs at airports:\n", dropoffs_at_airports)

# What is the total amount of airport fees collected at each NYC airport? (JFK and LaGuardia)
airport_fees = df1[df1['Zone_PU'].isin(['JFK Airport', 'LaGuardia Airport'])]['airport_fee'].sum()
print("Total airport fees collected:\n", airport_fees)

# What borough destination had the most tips?
borough_most_tips = df1.groupby('Borough_DO')['tip_amount'].sum().idxmax()
print("Borough with the most tips:\n", borough_most_tips)

# Top 10 pickup locations by number of passengers
top_10_pickup_locations = df1.groupby('Zone_PU')['passenger_count'].sum().nlargest(10)
print("Top 10 pickup locations by number of passengers:\n", top_10_pickup_locations)

# Visualization: Top 10 pickup locations by number of passengers
top_10_pickup_locations.plot(kind='bar', figsize=(10, 6))
plt.title('Top 10 Pickup Locations by Number of Passengers')
plt.xlabel('Pickup Locations')
plt.ylabel('Number of Passengers')
plt.xticks(rotation=45, ha='right')
plt.show()
