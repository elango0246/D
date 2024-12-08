from mpl_toolkits import basemap
import matplotlib.pyplot as plt
latitudes = [228,39,40]
longitudes = [77,66,44,33]

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
x, y = m(longitudes, latitudes)

# Plot data points
m.scatter(x, y, s=10, c='red', marker='o', alpha=0.6, label='Restaurants')

# Add legend and title
plt.legend(loc='lower left')
plt.title('Zomato Restaurant Locations')
plt.show()