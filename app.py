from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>HI I AM AVINASH </h1>
    <h2>I AM STUDENT OF MAHESH SIR</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)