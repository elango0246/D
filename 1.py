import matplotlib.pyplot as plt
import pandas as pd

data = {
    "OZONE": [41, 36, 12, 1, 18, 28],
    "SOLAR": [190, 118, 149, 313, 2, 3],
    "TEMP": [7.4, 8.0, 12.6, 11.5, 14.3, 14.9],
    "WIND": [67, 72, 74, 62, 56, 66],
    "MONTH": [5, 5, 5, 5, 5, 5],
    "DAY": [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['DAY'], df['OZONE'])
plt.title('Bar Plot of OZONE Levels')
plt.xlabel('Day')
plt.ylabel('OZONE')
plt.show()

plt.barh(df['DAY'], df['SOLAR'], color='orange')
plt.title('Vertical Bar Plot of SOLAR Radiation')
plt.xlabel('SOLAR')
plt.ylabel('Day')
plt.show()

plt.scatter(df['TEMP'], df['WIND'], color='red')
plt.title('Scatter Plot of TEMP vs WIND')
plt.xlabel('TEMP')
plt.ylabel('WIND')
plt.show()

plt.hist(df['TEMP'], bins=5 , color='green')
plt.title('Histogram of TEMP')
plt.xlabel('TEMP')
plt.ylabel('Frequency')
plt.show()
