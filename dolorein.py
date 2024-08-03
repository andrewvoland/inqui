from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Example dataset
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.randint(0, 2, 100)  # Binary classification (0 or 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Calculate baseline accuracy on the test set
y_pred = model.predict(X_test)
baseline_accuracy = accuracy_score(y_test, y_pred)

print(f"Baseline Accuracy: {baseline_accuracy:.2f}")

# Check if baseline accuracy is less than 0.5
if baseline_accuracy < 0.5:
    print("Baseline accuracy is too low. Consider revising your model or dataset.")
    # Additional actions like logging, retraining, etc.
else:
    print("Baseline accuracy is acceptable. Proceed with further analysis or steps.")
