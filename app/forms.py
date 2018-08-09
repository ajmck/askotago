from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = StringField("PostContent", validators=[DataRequired()])
    submit = SubmitField("Submit")
