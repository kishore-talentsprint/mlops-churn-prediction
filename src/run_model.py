import pickle

# Load the pre-trained model
with open('models/churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Interactive user input
print("Enter the following customer details to get a churn prediction:")
credit_score = float(input("Credit Score: "))
age = float(input("Age: "))
balance = float(input("Balance: "))
products_number = int(input("Number of Products: "))
has_credit_card = int(input("Has Credit Card (1 for Yes, 0 for No): "))
is_active_member = int(input("Is Active Member (1 for Yes, 0 for No): "))
estimated_salary = float(input("Estimated Salary: "))

# Model prediction
features = [[credit_score, age, balance, products_number, has_credit_card, is_active_member, estimated_salary]]
prediction = model.predict(features)

# Output the result
result = "Churn" if prediction[0] == 1 else "No Churn"
print(f"Prediction: {result}")
