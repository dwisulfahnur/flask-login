from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from forms import LoginForm
from models import User, db
from flask.views import MethodView
from werkzeug.security import check_password_hash
from functools import wraps
user_views = Blueprint('user_views', __name__, template_folder='../../templates',
                                         static_folder='../../static'
                                         )


@user_views.route('/home/')
def home():
    user = User.query.filter_by(id = session['user_id']).first()
    return render_template('home.html', user=user)

@user_views.route('/login/', methods=['POST', 'GET'])
def login():
    if 'user_id' in session:
        return redirect(url_for('.home'))
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                    session['user_id'] = user.id
                    return redirect(url_for('.home'))
            error = 'Invalid Password'
        else:
            error='Unknown Username.'

    return render_template('login.html', form=form, error=error)



@user_views.route('/logout/')
def logout():
    session.pop('user_id', None)
    flash('You\'re Logged out')
    return redirect(url_for('.login'))
