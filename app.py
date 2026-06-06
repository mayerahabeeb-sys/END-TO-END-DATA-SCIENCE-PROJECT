from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

with open("model.pkl",      "rb") as f: model      = pickle.load(f)
with open("vectorizer.pkl", "rb") as f: vectorizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result  = None
    message = ""
    if request.method == "POST":
        message   = request.form["message"]
        vec       = vectorizer.transform([message])
        pred      = model.predict(vec)[0]
        result    = "🚨 SPAM" if pred == "spam" else "✅ NOT SPAM"
    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)