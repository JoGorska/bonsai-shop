"""form for super user to add products"""
# pylint: disable=no-member
from django import forms
from .models import Tree, Feature, Enviroment


class TreeForm(forms.ModelForm):
    """
    Form to add trees to the shop
    """
    class Meta:
        """
        Meta data for product form
        """
        model = Tree
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        features = Feature.objects.all()
        f_friendly_names = [(f.id, f.get_friendly_name()) for f in features]
        enviroments = Enviroment.objects.all()
        e_friendly_names = [(e.id, e.get_friendly_name()) for e in enviroments]

        self.fields['feature'].choices = f_friendly_names
        self.fields['enviroment'].choices = e_friendly_names
