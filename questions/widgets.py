"""gets template from django for custom clearable input"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    gets template from django for custom clearable input
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'questions/custom_widget_templates/custom_clearable_file_input.html')
