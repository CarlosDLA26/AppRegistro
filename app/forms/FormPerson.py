from wtforms.fields import(
    StringField,
    SubmitField,
    EmailField
)
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class FormPerson(FlaskForm):

    """Formulario para registrar a las personas
    en la base de datos mydatabase.sqlite

    Se valida que el nombre y ciudad sean strings
    y se verifica que el email tenga el formato de un
    correo electrónico
    """

    name = StringField('Nombre completo', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    submit = SubmitField('Enviar')