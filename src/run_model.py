import os
import pickle

def load_model():
    model_path = os.path.join('models', 'churn_model.pkl')
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def get_customer_input():
    credit_score = float(input("Enter credit score: "))
    age = int(input("Enter age: "))
    balance = float(input("Enter balance: "))
    number_of_products = int(input("Enter number of products: "))
    # Add other fields as necessary
    return [[credit_score, age, balance, number_of_products]]

def predict_churn(model, customer_data):
    prediction = model.predict(customer_data)
    return prediction[0]

if __name__ == "__main__":
    model = load_model()
    customer_data = get_customer_input()
    result = predict_churn(model, customer_data)
    print("Churn Prediction:", "Will Churn" if result == 1 else "Will Not Churn")
