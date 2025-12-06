# model.py
from sklearn.linear_model import LogisticRegression

def build_model():
    model = LogisticRegression()
    return model

if __name__ == "__main__":
    clf = build_model()
    print("Model created:", clf)
