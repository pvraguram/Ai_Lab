from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Training data: Outlook, Temperature
X = [
    ["Sunny", "Hot"],
    ["Sunny", "Cool"],
    ["Rainy", "Hot"],
    ["Rainy", "Cool"],
    ["Overcast", "Hot"],
    ["Overcast", "Cool"]
]

# Output classes
y = ["No", "No", "Yes", "Yes", "Yes", "Yes"]

# Convert text into numbers
encoders = []

for col in range(2):
    encoder = LabelEncoder()
    column = [row[col] for row in X]
    encoder.fit(column)

    for row in X:
        row[col] = encoder.transform([row[col]])[0]

    encoders.append(encoder)

# Train the classifier
model = GaussianNB()
model.fit(X, y)

# Get input from the user
outlook = input("Enter outlook (Sunny/Rainy/Overcast): ")
temperature = input("Enter temperature (Hot/Cool): ")

# Encode the input
test = [[
    encoders[0].transform([outlook])[0],
    encoders[1].transform([temperature])[0]
]]

# Predict the class
prediction = model.predict(test)

print("Predicted class:", prediction[0])