from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
class Form(FlaskForm):

	Name=StringField('Name',validators=[DataRequired("PLease Enter your Name.")])
	Password=PasswordField('Password',validators=[DataRequired("PLease Enter your Password.")])
	submit=SubmitField('signIn')