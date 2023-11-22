from flask import Flask, render_template, request, jsonify

from chat import get_response
app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response1 = get_response(text)
    message1 = {"answer": response1}
    return jsonify(message1)

if __name__ == "__main__":
    app.run(debug=True)
