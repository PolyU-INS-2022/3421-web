from flask import Flask, render_template, make_response, request, redirect
from flask_login import current_user, login_required, logout_user
from flask_wtf.csrf import CSRFProtect

from auth import register, login_manager, login, get_user
from db import db
from memorial import create_memorial


app = Flask(__name__)
app.secret_key = "d6cf28f632b5e1b52e476817a306446154841aea065217409a7e136d0b73a0f7277181c7a18afad7cf67e2e8b9ddf9341073034c039f17ad61cbcd227123259f"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SESSION_COOKIE_SAMESITE"] = "Strict"


csrf = CSRFProtect(app)
db.init_app(app)
login_manager.init_app(app)
with app.app_context():
    db.create_all()


@app.template_filter()
def pretty_time(time):
    return time.strftime("%H:%M:%S")


@app.template_filter()
def pretty_time2(time):
    return str(time).rjust(2, "0")


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("/welcome")
    else:
        return redirect("/memorial")


@app.route("/memorial")
def memorial():
    return make_response(render_template("memorial.html"))


@app.route("/memorial/create", methods=["GET", "POST"])
def memorial_create():
    if request.method == "POST" and create_memorial():
        return make_response(redirect("/heaven"))
    return make_response(render_template("create_memorial.html"))


@app.route("/welcome")
def welcome():
    return make_response(render_template("welcome.html"))


@app.route("/forums")
def forums():
    return make_response(render_template("forums.html"))


@app.route("/features")
def features():
    return make_response(render_template("features.html"))


@app.route("/heaven")
def heaven():
    return make_response(render_template("heaven.html"))


@app.route("/faq")
def faq():
    return make_response(render_template("faq.html"))


@app.route("/price")
def price():
    return make_response(render_template("price.html"))


@app.route("/register", methods=["GET", "POST"])
def request_register():
    if current_user.is_authenticated:
        return make_response(redirect("/"))
    if request.method == "POST":
        resp = register(request.form, db)
    else:
        resp = render_template("register.html")
    return make_response(resp)


@app.route("/login", methods=["GET", "POST"])
def request_login():
    if request.method == "GET":
        return make_response(render_template("login.html"))
    if login():
        resp = redirect("/welcome")
    else:
        resp = render_template('login.html', errors=[
                               "Wrong password or Login Id not exists"])
    return make_response(resp)


@app.route("/logout")
@login_required
def request_logout():
    logout_user()
    return make_response(redirect("/memorial"))


if __name__ == "__main__":
    app.run(debug=True, port=5555, host='0.0.0.0')
