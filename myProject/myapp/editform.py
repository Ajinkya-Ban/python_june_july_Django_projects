from django import forms
from.models import Register

class EditUserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'