import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv(r'C:\Users\IMAM HOSSAIN\OneDrive - MSFT\Desktop\FastApiCode\heart.csv')
data
x = data.drop('target', axis=1)
y = data['target']
print(x.head(), y.head())


# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

#save the model to a joblib file
joblib.dump(model, 'model/heart_disease_model.joblib')

print("Model trained and saved successfully.")