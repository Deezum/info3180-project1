from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    # Attributes
    proptitle = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    room = StringField('No. of Rooms', validators=[DataRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[DataRequired()])
    propprice = StringField('Price', validators=[DataRequired()])
    proptype = SelectField('Property Type', choices=[
                         ('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    picup = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])