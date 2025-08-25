from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "mushroom_model.pkl")


# Load tree (dict)
with open(MODEL_PATH, "rb") as f:
    tree = pickle.load(f)

# ------------------------
# Hàm dự đoán theo ID3 tree
# ------------------------
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "e"

# ------------------------
# Thuộc tính (mapping label → mô tả)
# ------------------------
feature_columns = {
    "cap-shape": {
        "b": "Bell (Chuông)",
        "c": "Conical (Nón)",
        "x": "Convex (Lồi)",
        "f": "Flat (Phẳng)",
        "k": "Knobbed (Có núm)",
        "s": "Sunken (Lõm)"
    },
    "cap-surface": {
        "f": "Fibrous (Sợi)",
        "g": "Grooves (Rãnh)",
        "y": "Scaly (Vảy)",
        "s": "Smooth (Nhẵn)"
    },
    "cap-color": {
        "n": "Brown (Nâu)",
        "b": "Buff (Vàng nhạt)",
        "c": "Cinnamon (Quế)",
        "g": "Gray (Xám)",
        "r": "Green (Xanh lá)",
        "p": "Pink (Hồng)",
        "u": "Purple (Tím)",
        "e": "Red (Đỏ)",
        "w": "White (Trắng)",
        "y": "Yellow (Vàng)"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        shape = request.form["cap-shape"]
        surface = request.form["cap-surface"]
        color = request.form["cap-color"]

        sample = {
            "cap-shape": shape,
            "cap-surface": surface,
            "cap-color": color
        }

        prediction = predict(tree, sample)
        result = "🍄 Nấm Ăn được" if prediction == "e" else "☠️ Nấm Độc / Không ăn được"

    return render_template("index.html", result=result, feature_columns=feature_columns)

if __name__ == "__main__":
    app.run(debug=True)
