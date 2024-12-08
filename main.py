import pandas as pd
import matplotlib.pyplot as plt
(r"C:\Users\LENOVO\Downloads\zomato_data.csv")
from mpl_toolkits.basemap import Basemap

# Load Zomato data (replace the path with your file's location)
zomato_data = pd.read_csv(r"C:\Users\LENOVO\Downloads\zomato_data.csv")

# Check and clean data
print(zomato_data.columns)  # Verify column names
zomato_data = zomato_data.dropna(subset=['latitude', 'longitude'])  # Drop rows with missing lat/lon

# Initialize the map
plt.figure(figsize=(12, 8))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

# Draw map features
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgreen', lake_color='aqua')

# Convert latitude and longitude to map coordinates
x, y = m(zomato_data['longitude'].values, zomato_data['latitude'].values)

# Plot Zomato locations
m.scatter(x, y, s=10, c='red', alpha=0.7, marker='o', label='Zomato Locations')

# Add legend and title
plt.legend(loc='lower left')
plt.title("Zomato Locations on World Map", fontsize=15)
plt.show()
