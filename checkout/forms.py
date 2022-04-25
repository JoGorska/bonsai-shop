'''forms for checkout app'''
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
    order form
    '''
    class Meta:
        '''
        meta data - which model the form reffers to
        which fields from the model we want to render
        NOT rendering the fields that will be automaticaly calculated
        '''
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        overrides form __init__ method
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # adds nice placeholders
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # sets autofocus on full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # makes country readonly
        self.fields['country'].widget.attrs['readonly'] = True

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # ads a star for fields that are required on the model
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # sets attributes for place holder and class and removes labels
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
