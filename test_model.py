import pytest
import numpy as np
from src.load_model import load_model
from src.run_model import predict_churn
import xgboost

def test_load_model():
    model = load_model()    
    assert isinstance(model, xgboost.sklearn.XGBClassifier)

def test_predict_churn():
    model = load_model()
    customer_data = [[120, 1, 0, 25, 2, 1000, 2, 1]]

    pred = predict_churn(model, customer_data)

    assert isinstance(pred, np.int64)
    assert pred<2 and pred>=0



