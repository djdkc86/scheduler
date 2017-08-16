from __future__ import unicode_literals
from django import forms
from .models import User, Person, Role

class Login(forms.Form):
	username = forms.CharField(max_length=255,label='Username')
	password = forms.CharField(max_length=50, label='Password')

	class Meta:
		model = User

class CreateUser(forms.Form):
	fname = forms.CharField(max_length=50)
	lname = forms.CharField(max_length=50)
	role = forms.ModelChoiceField(Role.objects.all())
	password = forms.CharField(max_length=50)

	class Meta:
		model = Person
