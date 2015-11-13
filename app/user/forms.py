from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from models import User
from werkzeug.security import check_password_hash
class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def validate_login(self):
        user = User.query.filter_by(username = self.username.data).first()
        if user:
            if check_password_hash(user.password, self.password.data ):
                #return 'Hai %s, Its Page for User Area'%(user.username)
                self.user = user
                return True
            else:
                self.error = 'Invalid Password'
        else:
            self.error='Unknown Username'
