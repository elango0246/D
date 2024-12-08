import pandas as pd
import matplotlib.pyplot as plt

# Sample Time Series Data: Daily temperatures for a month
data = {
    "Date": pd.date_range(start="2024-11-01", periods=30, freq="D"),

    "Temperature": [22, 23, 21, 20, 22, 23, 24, 25, 24, 23, 22, 21, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 30, 29, 28, 27, 26, 25]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting the time series data
plt.plot(df["Date"], df["Temperature"], marker='o', color='b', label="Temperature (°C)")

# Adding title and labels
plt.title("Daily Temperature Over One Month")
plt.xlabel("Date",)
plt.ylabel("Temperature (°C)",)
plt.grid(True)


# Show the plot

plt.show()
