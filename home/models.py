# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	id = models.BigIntegerField(primary_key=True, unique=True)
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	role = models.ForeignKey('Role')
	username = models.ForeignKey('User')
	class Meta:
		db_table = 'instructor'
	def __str__(self):
		return '{} {}'.format(self.fname, self.lname)

class Role(models.Model):
	id = models.BigIntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=50)
	class Meta:
		db_table = 'role'
	def __str__(self):
		return self.name

class User(models.Model):
	username = models.CharField(primary_key=True, unique=True, max_length=255)
	password = models.CharField(max_length=20)
	class Meta:
		db_table = 'user'
	def __str__(self):
		return self.username


class Room(models.Model):
	id = models.BigIntegerField(primary_key=True, unique=True)
	room = models.CharField(max_length=50)
	class Meta:
		db_table = 'room'
	def __str__(self):
		return self.room

class Location(models.Model):
	id = models.BigIntegerField(primary_key=True, unique=True)
	location = models.CharField(max_length=50)	
	class Meta:
		db_table = 'location'
	def __str__(self):
		return self.location

#class Schedule(models.Model):
#	id = models.BigIntegerField(primary_key=True, unique=True)
#	person = models.ForeignKey('person', related_name='person',null=True, blank=True)
#	course1= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course2= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course3= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course4= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course5= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course6= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	course7= models.ForeignKey('course',related_name='course',null=True, blank=True)
#	class Meta:
#		db_table = 'schedule'
#	def __str__(self):
#		return '{}{}'.format(self.person, self.id)

class Course(models.Model):
	id = models.BigIntegerField(primary_key=True, unique=True)
	classname = models.CharField(max_length=50,blank=True,null=True)
	days = models.CharField(max_length=50,blank=True,null=True)
	timestart = models.CharField(max_length=50,blank=True,null=True)
	endtime = models.CharField(max_length=50,blank=True,null=True)
	room = models.ForeignKey('Room',null=True, blank=True)
	location = models.ForeignKey('Location',null=True, blank=True)
	#instructor = models.ForeignKey('person',related_name='person',null=True, blank=True)

	class Meta:
		db_table = 'course'

	def __str__(self):
		return classname