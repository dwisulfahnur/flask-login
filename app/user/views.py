from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from forms import LoginForm
from models import User, db
from flask.views import MethodView
from werkzeug.security import check_password_hash
from functools import wraps
user_views = Blueprint('user_views', __name__, template_folder='../../templates',
                                         static_folder='../../static'
                                         )

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            flash('You need To login first.')
            return redirect(url_for('.login'))
    return wrap

@user_views.route('/home/')
@login_required
def home():
    user = User.query.filter_by(id = session['user_id']).first()
    return render_template('home.html', user=user)

@user_views.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            session['user_id'] = form.user.id
            return redirect(url_for('.home'))
    return render_template('login.html', form=form)

@user_views.route('/logout/')
@login_required
def logout():
    session.pop('user_id', None)
    flash('You\'re Logged out')
    return redirect(url_for('.login'))
