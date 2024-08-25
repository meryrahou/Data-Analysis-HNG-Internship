import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
file_path = './Stage8/Data.xlsx'
sheets = pd.read_excel(file_path, sheet_name=None)

# Extract individual sheets
germany_df = sheets['Germany']
africa_df = sheets['Africa']
projection_df = sheets['Sheet3']

# Step 1: Clean and Prepare Data (Germany)

# Calculate Retiring Doctors per year
# Assuming '65 to 74 years' corresponds to the retirement age group
germany_df['Retiring Doctors'] = germany_df['65 to 74 years']  # Using the count of doctors in the 65-74 age group

# Calculate New Doctors entering the workforce
germany_df['New Doctors'] = germany_df['Grad per 1000 practicing'] * (germany_df['Persons(Practing)'] / 1000)

# Calculate Net Immigration of doctors
germany_df['Net Immigration'] = germany_df['Inflow Immigration'] - germany_df['Outflow Immigration']

# Calculate Doctor Deficit
germany_df['Doctor Deficit'] = germany_df['Retiring Doctors'] - germany_df['New Doctors'] + germany_df['Net Immigration']

# Step 2: Plot Doctor Deficit in Germany
plt.figure(figsize=(10, 6))
sns.lineplot(x=germany_df['YEAR'], y=germany_df['Doctor Deficit'])
plt.title('Projected Doctor Deficit in Germany Over the Next 20 Years')
plt.xlabel('Year')
plt.ylabel('Doctor Deficit')
plt.grid(True)
plt.savefig('doctor_deficit_germany.png')  # Save the plot
plt.show()

# Step 3: Analyze the Impact on Africa
# Example calculation for Doctor Migration to Germany from Africa
# Assume that some portion of the population in Africa migrates to Germany as doctors

# Using an arbitrary factor for migration; adjust as needed
africa_df['Doctor Migration to Germany'] = africa_df['POP(AFRICA)'] * 0.0001  # Replace 0.0001 with a more realistic factor

# Estimate Impact on Africa
africa_df['Impact on Africa'] = africa_df['POP(AFRICA)'] - africa_df['Doctor Migration to Germany']

# Step 4: Plot Impact on Africa
plt.figure(figsize=(10, 6))
sns.lineplot(x=africa_df['YEAR'], y=africa_df['Impact on Africa'])
plt.title('Impact on Africa Due to Doctor Migration to Germany')
plt.xlabel('Year')
plt.ylabel('Impact on Africa')
plt.grid(True)
plt.savefig('impact_on_africa.png')  # Save the plot
plt.show()

# Step 5: Save the updated DataFrames to CSV files
germany_df.to_csv('germany_doctor_deficit.csv', index=False)
africa_df.to_csv('africa_impact.csv', index=False)

print("Analysis complete. Files and graphs saved successfully.")
