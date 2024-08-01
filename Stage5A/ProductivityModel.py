import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = './Stage5/USA/MergedData.csv'
data = pd.read_csv(file_path)

# Ensure 'Date' column is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Drop any rows with NaN values (if 'Date' conversion fails or other columns have NaNs)
data.dropna(inplace=True)

# Calculate Productivity
data['Productivity'] = data['SharePrice'] / (data['Inflation'] * data['M1SL'])

# Plot productivity over time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Productivity'], label='Productivity', color='blue')
plt.xlabel('Date')
plt.ylabel('Productivity')
plt.title('Productivity Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the productivity plot to the Visual folder
productivity_plot_path = './Stage5/USA/Visuals/ProductivityOverTime.png'
plt.savefig(productivity_plot_path)

plt.show()


