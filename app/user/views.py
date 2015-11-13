from flask import Blueprint, render_template, request, redirect, url_for, session
from forms import LoginForm
from models import User, db
from flask.views import MethodView
from werkzeug.security import check_password_hash
user_views = Blueprint('user', __name__, template_folder='../../templates',
                                         static_folder='../../static'
                                         )
@user_views.route('/home/')
def home():
    return 'it\'s User Area: %s'

@user_views.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_login() == True:
            return 'Hai %s, Its Page for User Area'%(form.user.username)
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)
