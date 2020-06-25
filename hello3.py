from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/example")
# def example():
#     return "This is the example page:)"


@app.route("/example/<username>")
def example(username):
    return "This is the example page for %s." % username


@app.route("/show/<int:_id>")
def show_number(_id):
    return "%d × %d = %d" % (_id, _id, _id * _id)


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath %s" % subpath


if __name__ == "__main__":
    app.run()
