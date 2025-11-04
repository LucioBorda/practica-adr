from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hola, el deploy con GitHub Actions y Flask funciona perfectamente!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
