import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Wine Quality dataset
df = pd.read_csv(r'C:\Users\LENOVO\Downloads\winequality.csv')  # Replace with your CSV file path

# Display basic information
print("Dataset Information:")
print(df.info())

# Show basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize the distribution of wine quality
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='quality')
plt.title("Distribution of Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Count")
plt.show()

# Visualize feature distributions (histograms)
df.hist(bins=15,  color='skyblue', edgecolor='black')
plt.suptitle('Feature Distributions')

plt.show()

# Correlation heatmap
