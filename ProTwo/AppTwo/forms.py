from django import forms
from AppTwo.models import user

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Your email one more time:')
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email should match")

class FormUser(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
