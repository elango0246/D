import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
emails = pd.read_csv(r'C:\Users\LENOVO\Downloads\sample_emails.csv')  # Adjust path if necessary

# Check dataset structure
print(emails.info())

# Add a length column for the email body
emails['length'] = emails['Body'].apply(len)  # Replace 'Body' with your actual column name

# Plot a histogram of the lengths
plt.hist(emails['length'],bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Email Body Lengths')
plt.xlabel('Length of Email Body')
plt.ylabel('Frequency')
plt.show()
