
# Decision Tree Implementation without External Libraries

# Dataset: [Age, Salary, Buys_Product]
data = [
    [22, 20000, "No"],
    [25, 25000, "No"],
    [47, 50000, "Yes"],
    [52, 60000, "Yes"],
    [46, 45000, "Yes"],
    [56, 70000, "Yes"],
    [23, 22000, "No"],
    [40, 40000, "No"],
    [60, 80000, "Yes"],
    [48, 55000, "Yes"]
]

# Create Decision Tree
def decision_tree(age, salary):
    if age <= 30:
        return "No"
    elif salary <= 40000:
        return "No"
    else:
        return "Yes"


# Display Dataset
print("DECISION TREE CLASSIFICATION")
print("--------------------------------")

print("Age\tSalary\t\tBuys Product")
for row in data:
    print(row[0], "\t", row[1], "\t\t", row[2])

# Test Predictions
print("\nPREDICTIONS")
print("--------------------------------")

test_data = [
    [25, 30000],
    [45, 50000],
    [35, 25000],
    [55, 70000]
]

for person in test_data:
    result = decision_tree(person[0], person[1])

    print("Age:", person[0],
          "Salary:", person[1],
          "Prediction:", result)

print("\nDecision Tree completed successfully!")

