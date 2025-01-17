from django import forms
from.models import Register

class EditUserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False  # Make the address field optional