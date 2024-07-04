import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic

# Load the dataset with all required information
df = pd.read_csv('./Stage1/geocoded_data.csv')

print("DataFrame columns:", df.columns)

# Extract latitude and longitude columns directly from the DataFrame
lat_lon = df[['Latitude', 'Longitude']].values

radius_km = 1

# Compute geodesic distance matrix
def geodesic_distance_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = geodesic(locations[i], locations[j]).km
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist
    return dist_matrix

geo_dist_matrix = geodesic_distance_matrix(lat_lon)

# Calculate the outlier scores for each polling unit
results = []
for index, row in df.iterrows():
    neighbors = df[(geo_dist_matrix[index] <= radius_km) & (df.index != index)]

    apc_outlier = abs(row['APC'] - neighbors['APC'].mean()) if not neighbors.empty else 0
    lp_outlier = abs(row['LP'] - neighbors['LP'].mean()) if not neighbors.empty else 0
    pdp_outlier = abs(row['PDP'] - neighbors['PDP'].mean()) if not neighbors.empty else 0
    nnpp_outlier = abs(row['NNPP'] - neighbors['NNPP'].mean()) if not neighbors.empty else 0

    results.append({
        'PU-Code': row['PU-Code'],
        'PU-Name': row['PU-Name'],
        'Ward': row['Ward'],
        'Latitude': row['Latitude'],
        'Longitude': row['Longitude'],
        'APC_outlier': apc_outlier,
        'LP_outlier': lp_outlier,
        'PDP_outlier': pdp_outlier,
        'NNPP_outlier': nnpp_outlier,
        'Neighbors': neighbors['PU-Code'].tolist()
    })

outlier_scores = pd.DataFrame(results)


# Sort the dataset by the outlier scores for each party
sorted_apc = outlier_scores.sort_values(by='APC_outlier', ascending=False).head(3)
sorted_lp = outlier_scores.sort_values(by='LP_outlier', ascending=False).head(3)
sorted_pdp = outlier_scores.sort_values(by='PDP_outlier', ascending=False).head(3)
sorted_nnpp = outlier_scores.sort_values(by='NNPP_outlier', ascending=False).head(3)

output_file_path = 'outlier_scores.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    outlier_scores.to_excel(writer, sheet_name='Outlier Scores', index=False)
    sorted_apc.to_excel(writer, sheet_name='Top 3 APC Outliers', index=False)
    sorted_lp.to_excel(writer, sheet_name='Top 3 LP Outliers', index=False)
    sorted_pdp.to_excel(writer, sheet_name='Top 3 PDP Outliers', index=False)
    sorted_nnpp.to_excel(writer, sheet_name='Top 3 NNPP Outliers', index=False)

print(f"The outlier scores and top 3 outliers for each party have been saved to {output_file_path}")



# Visualization Part

# Box Plot for each party's outlier scores
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[['APC', 'LP', 'PDP', 'NNPP']])
plt.title('Box Plot of Votes by Party')
plt.xlabel('Party')
plt.ylabel('Votes')
plt.savefig('box_plot_votes_by_party.png')
plt.show()

# Scatter Plot for latitude vs longitude with outlier scores
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', hue='PDP_outlier', data=outlier_scores, palette='viridis', size='PDP_outlier', sizes=(20, 200))
plt.title('Scatter Plot of Polling Units (PDP Outlier Scores)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='PDP Outlier Score', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('scatter_plot_pdp_outliers.png')
plt.show()

# Histogram of PDP outlier scores
plt.figure(figsize=(12, 8))
sns.histplot(outlier_scores['PDP_outlier'], bins=30, kde=True)
plt.title('Histogram of PDP Outlier Scores')
plt.xlabel('Outlier Score')
plt.ylabel('Frequency')
plt.savefig('histogram_pdp_outlier_scores.png')
plt.show()
