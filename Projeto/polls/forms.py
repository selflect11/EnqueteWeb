from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = User
		fields = '__all__'
		widgets = {
			'password': forms.PasswordInput(),
		}
