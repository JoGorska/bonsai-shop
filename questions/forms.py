"""form for super user to add products"""
# pylint: disable=no-member
from django import forms
from .widgets import CustomClearableFileInput
from .models import Question


class QuestionForm(forms.ModelForm):
    """
    Form to add trees to the shop
    """
    class Meta:
        """
        Meta data for product form
        """
        model = Question
        fields = '__all__'
    # replaces default styling with customised styling of the image input
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
