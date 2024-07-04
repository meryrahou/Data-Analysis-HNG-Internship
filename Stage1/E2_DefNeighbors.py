import pandas as pd
from geopy.distance import geodesic

# Loading geocoded_data into DataFrame
df = pd.read_csv('./Stage1/geocoded_data.csv')

def find_neighbors(df, radius=5):
    neighbors = {}
    zero_neighbors = 0
    for i, row_i in df.iterrows():
        neighbors_list = []
        for j, row_j in df.iterrows():
            if i != j:
                distance = geodesic((row_i['Latitude'], row_i['Longitude']), (row_j['Latitude'], row_j['Longitude'])).kilometers
                if distance <= radius:
                    neighbors_list.append(j)
        neighbors[i] = neighbors_list
        if len(neighbors_list) == 0:
            zero_neighbors += 1
    return neighbors, zero_neighbors

neighbors, zero_neighbors = find_neighbors(df)
print(f"Found {zero_neighbors} points with no neighbors.")

# Convert neighbors dictionary to a DataFrame for saving
neighbors_df = pd.DataFrame(list(neighbors.items()), columns=['Point', 'Neighbors'])

# Convert list of neighbors to a string representation for CSV storage
neighbors_df['Neighbors'] = neighbors_df['Neighbors'].apply(lambda x: ','.join(map(str, x)))

# Save to CSV
neighbors_df.to_csv('./Stage1/neighbors_5Radius.csv', index=False)