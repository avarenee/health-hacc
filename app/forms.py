from flask-wtf import Flaskform
from wtforms import StringFrield, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RetrievalForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
        address = StringField('Address', validators=[DataRequired()])
	submit = SubmitField('Submit')
