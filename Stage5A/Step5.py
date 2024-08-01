import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = './Stage5/USA/MergedData.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index('Date')

# Calculate percentage change and real devaluation
data['M1SL_Change'] = data['M1SL'].pct_change() * 100
data['Real_Devaluation'] = data['M1SL_Change'] - data['Inflation']

# Plotting
plt.figure(figsize=(12, 8))

# Plot M1SL Change
plt.subplot(3, 1, 1)
plt.plot(data.index, data['M1SL_Change'], label='M1SL Percentage Change', color='blue')
plt.title('Percentage Change in M1SL')
plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.legend()

# Plot Inflation
plt.subplot(3, 1, 2)
plt.plot(data.index, data['Inflation'], label='Inflation Rate', color='red')
plt.title('Inflation Rate')
plt.xlabel('Date')
plt.ylabel('Inflation (%)')
plt.legend()

# Plot Real Devaluation
plt.subplot(3, 1, 3)
plt.plot(data.index, data['Real_Devaluation'], label='Real Currency Devaluation', color='green')
plt.title('Real Currency Devaluation')
plt.xlabel('Date')
plt.ylabel('Real Devaluation')
plt.legend()

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('./Stage5/USA/Visuals/DevaluationAnalysis.png')  
plt.show()
