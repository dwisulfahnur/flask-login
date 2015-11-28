from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms import LoginForm
from models import User
from werkzeug.security import check_password_hash
from flask.ext.login import current_user, login_user, logout_user, login_required
user_views = Blueprint('user_views', __name__, template_folder='../../templates',
                                         static_folder='../../static'
                                         )


@user_views.route('/home/')
@login_required
def home():
    user = current_user
    return render_template('home.html', user=user)

@user_views.route('/login/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('.home'))
            error = 'Invalid Password'
        else:
            error='Unknown Username.'

    return render_template('login.html', form=form, error=error)



@user_views.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You\'re Logged out')
    return redirect(url_for('.login'))
