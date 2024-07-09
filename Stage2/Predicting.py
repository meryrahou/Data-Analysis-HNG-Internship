from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Load the dataset
df = pd.read_csv('./Stage2/Updated.csv')

df = pd.get_dummies(df, columns=['Precipitation type'])

# Define features and target variable
X = df.drop(['Flood', 'Date'], axis=1)  
y = df['Flood']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))


new_data = pd.DataFrame({
    'Precipitation': [25.0],                     
    'Precipitation probability': [0.5],          
    'Precipitation cover': [0.3],                
    'Precipitation type': 'rain',              
    'Sea level pressure': [1015.0]               
})

# Predict flood occurrence
future_predictions = model.predict(new_data)
print("\nFuture Predictions:")
print(future_predictions)
