import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load the Zomato dataset

data = pd.read_csv(r"C:\Users\LENOVO\Downloads\zomato_data.csv")

# Preview the dataset
print(data.head())

# Ensure the dataset has 'Latitude' and 'Longitude' columns
if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
    raise ValueError("Dataset must include 'Latitude' and 'Longitude' columns")

# Extract latitudes and longitudes
latitudes = data['Latitude']
longitudes = data['Longitude']

# Initialize Basemap
plt.figure(figsize=(12, 8))
m = Basemap(projection='merc',
            llcrnrlat=min(latitudes) - 1, urcrnrlat=max(latitudes) + 1,
            llcrnrlon=min(longitudes) - 1, urcrnrlon=max(longitudes) + 1,
            resolution='i')

# Draw map details
m.drawcoastlines()
m.drawcountries()
m.drawstates()


# Convert lat/lon to map coordinates
x, y = m(longitudes.values, latitudes.values)

# Plot data points
m.scatter(x, y, s=10, c='red', marker='o', alpha=0.6, label='Restaurants')

# Add legend and title
plt.legend(loc='lower left')
plt.title('Zomato Restaurant Locations')
plt.show()
