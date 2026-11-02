
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Input data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Target output
y = np.array([[0],
              [1],
              [1],
              [0]])

# Create neural network
model = Sequential()

# Input layer and hidden layer
model.add(Dense(8, input_dim=2, activation='relu'))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Test the model
predictions = model.predict(X, verbose=0)

# Display results
print("Feed Forward Neural Network")
print("---------------------------")

for i in range(len(X)):
    print("Input:", X[i],
          "Predicted Output:", round(float(predictions[i][0])),
          "Actual Output:", y[i][0])

print("\nModel Accuracy:",
      model.evaluate(X, y, verbose=0)[1] * 100, "%")

