from django.forms import ModelForm, Form, ChoiceField, IntegerField, CharField, BooleanField
from BW.models import Bikes

# , bike_types

# import , TextField,

class FilterForm(Form):
    bike_type = ChoiceField(
        label='Filter by type:',
        choices=Bikes.bike_types, 
        required=False, 
        widget=ChoiceField.widget(attrs={'class': 'form-select'})
    )

class BikeInformationForm(Form):
    bike_type = ChoiceField(choices=Bikes.bike_types)
    name = CharField(max_length=25)
    description = CharField(max_length=1024)
    price = IntegerField()
    is_there_any = BooleanField()
    bike_amount = IntegerField()

class OrderForm(Form):
    pass

class ReviewForm(Form):
    review_description = CharField(max_length=1024)
    review_rating = IntegerField()