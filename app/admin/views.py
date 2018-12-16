from flask import render_template,request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from . import admin
from app.models import User
from datetime import datetime
from app import db

@admin.route("/", methods=['GET'])
def index():
    return redirect(url_for("admin.login"))

@admin.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@admin.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin.route('/authenticate', methods=['POST'])
def authenticate():
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user is not None and user.verify_password(request.form.get('password')):
        login_user(user)
        user.last_login_at = datetime.now()

        db.session.add(user)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('admin.home'))
    flash('Invalid username or password')
    return redirect(url_for('admin.login'))

@admin.route("/home", methods=['GET'])
@login_required
def home():
    return render_template("base.html")


@admin.route("/employee-management",methods=['GET'])
@login_required
def show_employee_management():
    return render_template("employee_management.html")