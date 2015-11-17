from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from models import User
from werkzeug.security import check_password_hash
class LoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')

    def validate(self):
        user = User.query.filter_by(username = self.username.data).first()
        self.user = user

        if not user:
            self.username.errors = 'Unknown Username'
            if self.username.data == '':
                self.username.errors = 'Username can\'t empty'
            if self.password.data =='':
                self.password.errors = 'Password can\'t empty'
            return False
        else:
            if not check_password_hash(user.password, self.password.data):
                self.password.errors = 'Invalid Password'
                if self.password.data =='':
                    self.password.errors = 'Password can\'t empty'
                    return False
                return False
            return True
