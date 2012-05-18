from django import forms
from main.models import User, Tweet


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta: 
		model = User

class UserEditForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta: 
		model = User
		exclude = ('nick_name', 'email', 'birth_date',)

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet

class TweetEditForm(forms.ModelForm):
	class Meta: 
		model = Tweet
		exclude = ('owner',)