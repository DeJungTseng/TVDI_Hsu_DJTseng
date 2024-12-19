from flask import Flask,render_template,request,redirect,url_for
import datasource

import secrets
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from Lesson18_2 import app1
from auth import auth

# app:flask server
app = Flask(__name__)
app.config['SECRET_KEY']=secrets.token_hex(16)
app.register_blueprint(auth,url_prefix='/auth')

# app1:dash server
# middleware: server that integrate flask app and app1
application = DispatcherMiddleware(
    app,
    {"/dash": app1.server},
)

# the decorator app make the route to be html format
@app.route("/")
def index():
    return render_template("index.j2")

@app.route("/products")
def products():
    cities:list[dict]=datasource.get_cites()
    page = request.args.get('page',1, type=int)
    per_page = 10
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(cities) + per_page - 1 ) // per_page
    items_on_page = cities[start:end]
    return render_template('products.j2',
                           items_on_page=items_on_page,
                           total_pages=total_pages,
                           page = page)


@app.route("/pricing")
def pricing():
    cities:list[dict]=datasource.get_cites()
    page = request.args.get('page',1, type=int)
    per_page = 6
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(cities) + per_page - 1 ) // per_page
    items_on_page = cities[start:end]
    return render_template('pricing.j2',
                           items_on_page=items_on_page,
                           total_pages=total_pages,
                           page = page)



    


@app.route("/about")
def about():
    return render_template("about.j2")

@app.route("/success")
def success():
    return "<h1>登入成功</h1>"

if __name__ == "__main__":
    run_simple("localhost", 8080, application,use_debugger=True,use_reloader=True)