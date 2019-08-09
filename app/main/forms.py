from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,SelectField
from wtforms.validators import Required 



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class OrderForm(FlaskForm):
    Quantity = StringField('Pitch Title', validators=[Required()])
    Description = StringField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Hawaian','Hawaian'),('Something Meaty','Something Meaty'),('Chicken Peri Peri','Chicken Peri Peri')],validators=[Required()])
    cost = SubmitField('Add To Cart')