from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserOb(models.Model):
	userob_id	= models.AutoField(primary_key = True)
	user 	= models.OneToOneField(User)
		# username ..
		# password ..
		# email ..
		# first_name ..
		# last_name ..
	user_eduName	= models.CharField(max_length = 100, blank = True, null=True)
	user_compName   = models.CharField(max_length = 100, blank = True, null=True)
	user_dateTime	= models.DateTimeField(auto_now_add = True)
	user_eduClass	= models.IntegerField(default = 0)
	user_adminAbout = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return u'%s' % (self.user.username)

class QuestionOb(models.Model):
	question_id 	= models.AutoField(primary_key = True)
	question_text	= models.TextField()
	question_time 	= models.DateTimeField(auto_now_add = True)

	question_user   = models.ForeignKey(UserOb, on_delete = models.CASCADE)

	def __unicode__(self):
		return u'%s' % (self.question_text)

class AnswerOb(models.Model):
	answer_id 			= models.AutoField(primary_key = True)

	answer_question_id	= models.ForeignKey(QuestionOb, on_delete = models.CASCADE)
	answer_user_id		= models.ForeignKey(UserOb, on_delete = models.CASCADE)
	
	answer_content		= models.TextField()
	answer_date			= models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%s' % (self.answer_content)


