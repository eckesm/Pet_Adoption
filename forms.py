from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField,TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name", validators=[
                       InputRequired(message="Pet name is required.")])
    species = SelectField("Species", validators=[InputRequired(message="Species is required.")], choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(
        message="Please enter a valid URL.")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Age must be between 0 and 30.")])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL(
        message="Please enter a valid URL.")])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")
