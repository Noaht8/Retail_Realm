from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators
from wtforms.validators import ValidationError

def validate_image(form, field):
    if not field.data:
        raise ValidationError('Image is required.')
    if not ('jpg' in field.data.filename.lower() or 'png' in field.data.filename.lower() or 'jpeg' in field.data.filename.lower()):
        raise ValidationError('Only JPG, PNG, and JPEG images are allowed.') 



class AddProducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()] )
    colors = TextAreaField('Colors', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])