from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "This is the root page."


@app.route("/hello")
def example():
    return render_template("hell.html")


if __name__ == "__main__":
    app.run(debug=True)
