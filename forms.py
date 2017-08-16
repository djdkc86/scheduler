from __future__ import unicode_literals
from django import forms
from .models import *

class Login(forms.Form):
	username = forms.CharField(max_lengths=255,label='Username')
	password = forms.CharField(widget=PasswordInput(), max_length=50)

	class Meta:
		model = User

class CreateUser(forms.Form):
	fname = forms.CharField(max_length=50)
	lname = forms.CharField(max_length=50)
	role = forms.ModelChoiceField(Role.object.all())
	password = forms.CharField(max_length=50)


	class Meta:
		model = Person

