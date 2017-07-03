from django import forms


from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Password again', widget = forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username', 'first_name', 'last_name', 'email']

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('passwords do not match')
		return cd['password2'] 