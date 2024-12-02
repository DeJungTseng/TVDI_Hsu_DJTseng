from flask import Flask,render_template

app = Flask(__name__)

# the decorator app make the route to be html format
@app.route("/")
def index():
    return render_template("index.j2")

@app.route("/products")
def products():
    return render_template("products.j2")