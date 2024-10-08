from flask import Blueprint, render_template, request, session, redirect, abort, url_for
import config
from models.user import User
from extentions import db

app = Blueprint("admin", __name__)



@app.before_request
def before_request():
    if session.get('admin_login', None) == None and request.endpoint != "admin.login":
        abort(403)



@app.route('/admin/login' , methods = ["POST", "GET"])
def login():  # put application's code here

    if request.method == "POST":
        username = request.form.get('username',None)
        password = request.form.get('password',None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("admin/login")

    else:
        return render_template("admin/login.html")

@app.route('/admin/dashboard' , methods = ["GET"])
def dashboard():
    return render_template("admin/dashboard.html")

@app.route('/admin/dashboard/user_editor' , methods=["GET", "POST"])
def user_editor():
    if request.method == "GET":

        user = User.query.all()

        return render_template("admin/user_editor.html", user=user)
    else:
        username = request.form.get('username',None)
        email = request.form.get('email',None)
        phone = request.form.get('phone',None)

        p = User(username=username, email=email, phone=phone)
        db.session.add(p)
        db.session.commit()

        return "done"




@app.route('/admin/dashboard/edit/<id>' , methods=["GET", "POST"])
def edit_dashboard(id):
    user = User.query.filter(User.id == id).first_or_404()

    if request.method == "GET":

        return render_template("admin/edit.html", user=user)
    else:
        username = request.form.get('username',None)
        email = request.form.get('email',None)
        phone = request.form.get('phone',None)

        user.username = username
        user.email = email
        user.phone = phone

        db.session.commit()

        return redirect(url_for("admin.edit_dashboard", id=id))




@app.route('/admin/dashboard/PDF/<id>' , methods=["GET"])
def PDF_dashboard(id):
    if request.method == "GET":

        user = User.query.filter(User.id == id).first_or_404()

        return render_template("admin/PDF.html", user=user)
    else:
        username = request.form.get('username',None)
        email = request.form.get('email',None)
        phone = request.form.get('phone',None)

        p = User(username=username, email=email, phone=phone)
        db.session.add(p)
        db.session.commit()

        return "done"



