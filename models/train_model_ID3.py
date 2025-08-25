import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# ------------------------
# ID3 Implementation
# ------------------------
def entropy(y):
    values, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs))

def information_gain(X, y, feature):
    values, counts = np.unique(X[feature], return_counts=True)
    weighted_entropy = np.sum([
        (counts[i] / np.sum(counts)) * entropy(y[X[feature] == values[i]])
        for i in range(len(values))
    ])
    return entropy(y) - weighted_entropy

def id3(X, y, features):
    if len(np.unique(y)) == 1:
        return y.iloc[0]
    if len(features) == 0:
        return y.mode()[0]

    gains = [information_gain(X, y, f) for f in features]
    best_feature = features[np.argmax(gains)]

    tree = {best_feature: {}}
    for value in np.unique(X[best_feature]):
        sub_X = X[X[best_feature] == value]
        sub_y = y[X[best_feature] == value]
        remaining_features = [f for f in features if f != best_feature]
        tree[best_feature][value] = id3(sub_X, sub_y, remaining_features)
    return tree

# ------------------------
# Hàm dự đoán
# ------------------------
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "e"  # fallback: edible

# ------------------------
# Load dataset
# ------------------------
data = pd.read_csv("MushroomApp/data/mushrooms.csv")

X = data[["cap-shape", "cap-surface", "cap-color"]]
y = data["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

features = list(X_train.columns)
tree = id3(X_train, y_train, features)

# ------------------------
# Đánh giá
# ------------------------
y_pred = [predict(tree, X_test.iloc[i].to_dict()) for i in range(len(X_test))]

print("📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n📑 Classification Report:")
print(classification_report(y_test, y_pred, digits=4))
print(f"🎯 Accuracy: {(np.mean(y_pred == y_test)):.4f}")

# ------------------------
# Lưu mô hình (dict)
# ------------------------
with open("MushroomApp/models/mushroom_model.pkl", "wb") as f:
    pickle.dump(tree, f)

print("✅ Mô hình ID3 đã lưu tại MushroomApp/models/mushroom_model.pkl")
