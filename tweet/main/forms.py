from django import forms
from main.models import Profile, Tweet


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta: 
		model = Profile
		exclude = ('user', 'email', 'following')

class UserEditForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta: 
		model = Profile
		exclude = ('email', 'following')
	

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet

class TweetEditForm(forms.ModelForm):
	class Meta: 
		model = Tweet
		exclude= 'owner' 


