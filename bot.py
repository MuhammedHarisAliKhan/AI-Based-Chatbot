import flask
from transformers import pipeline

app = flask.Flask(__name__)

# Load GPT-2 model
chatbot = pipeline("text-generation", model="gpt2")

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user = flask.request.json["message"]

    prompt = (
        "You are a helpful university chatbot.\n"
        "Answer clearly and politely.\n"
        f"User: {user}\nBot:"
    )

    response = chatbot(
        prompt,
        max_length=120,
        temperature=0.7,
        do_sample=True
    )

    reply = response[0]["generated_text"]
    return flask.jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
    
    