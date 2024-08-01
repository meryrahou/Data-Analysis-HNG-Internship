import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = './Stage5/USA/MergedData.csv'
data = pd.read_csv(file_path)

# Drop non-numeric columns (like 'Date')
data_numeric = data.drop(columns=['Date'])

# Calculate the correlation matrix for numeric data only
correlation_matrix = data_numeric.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Economic Variables")
plt.show()

# Analyze time-shifted correlations for inflation with lags
for lag in range(1, 13):  # Analyze up to 12 months lag
    data_numeric[f'Inflation_lag_{lag}'] = data_numeric['Inflation'].shift(-lag)
    lagged_corr = data_numeric[['M1SL', 'SharePrice', f'Inflation_lag_{lag}']].corr()
    print(f'Correlation with Inflation Lag {lag} months:')
    print(lagged_corr)
    print()


# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Economic Variables")


# Save the figure
plot_path = './Stage5/USA/Visuals/CorrelationMatrix.png'
plt.savefig(plot_path)

plt.show()

# Calculate the baseline productivity (mean of all available data)
baseline_productivity = data['Productivity'].mean()
print(f'Baseline Productivity: {baseline_productivity}')