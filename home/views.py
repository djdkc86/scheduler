# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as uauth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import operator

# Create your views here.
def createuser(request):
	#u = request.session['user']
	#request.session['user'] = u
	if request.method =='POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			fname = form.cleaned_data['fname']
			lname = form.cleaned_data['lname']
			p = Person(fname=fname, lname=lname)
			p.role_id = role.pk
			p.save()
			name = fname[0]+lname
			iterate = 1
			while User.objects.filter(username = name).exists():
				name = name+iterate
				iterate = iterate + 1
			user = uauth.objects.create_user(username = name, password = form.cleaned_data['password'])
			user.save()
			return HttpResponseRedirect(reverse('home:login'))
	else:
		form = CreateUser()
	return render(request,'home/createuser.html', {'form':form,})

	def login(request):
		render("It worked")
