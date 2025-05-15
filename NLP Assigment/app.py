from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define label mapping
label_map = {
    -1: "Negative",
     0: "Neutral",
     1: "Positive"
}

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        comment = request.form["comment"]
        vectorized = vectorizer.transform([comment])
        prediction = model.predict(vectorized)[0]
        sentiment = label_map.get(prediction, "Unknown")
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
