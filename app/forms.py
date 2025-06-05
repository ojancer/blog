from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=100)])
    conteudo = TextAreaField('Conteúdo', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Publicar')
