from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class PaymentForm(FlaskForm):
    name = StringField('Ім\'я на карті', validators=[
        DataRequired(),
        Length(min=1, max=100)
    ])
    card_number = StringField('Номер картки', validators=[
        DataRequired(),
        Regexp(r'^\d{16}$', message="Номер картки повинен містити 16 цифр")
    ])
    expiry_date = StringField('Дата закінчення', validators=[
        DataRequired(),
        Regexp(r'^\d{2}/\d{2}$', message="Дата повинна бути у форматі MM/YY")
    ])
    cvv = StringField('CVV', validators=[
        DataRequired(),
        Regexp(r'^\d{3}$', message="CVV повинен містити 3 цифри")
    ])
    submit = SubmitField('Сплатити')
