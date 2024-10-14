import pickle
import os
import sys


from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

def load_model():
    model_path = os.path.join('models', 'churn_model.pkl')
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully.")
