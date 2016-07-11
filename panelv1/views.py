# -*- coding:utf- -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
import datetime

from panelv1.models import *

# Create your views here.

def login_page(request):
	login_error_u = False
	login_error_p = False
	if not request.user.is_authenticated():
		if request.method == 'POST':
			username 	= request.POST['username']
			password	= request.POST['password']

			if not username:
				login_error_u = True
			if not password:
				login_error_p = True
			else:
				user = authenticate(username=username, password=password)
				if user:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect('/boa-admin/index/')
					else:
						login_error_u = True
				else:
					login_error_u = True
		#else:
			# login_error = True
		context = {
			"login_error_u" : login_error_u,
			"login_error_p" : login_error_p,
		}
		return render(request, "login.html", context)
	else:
		return HttpResponseRedirect('/boa-admin/index/')

def index_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/boa-admin/')
	else:
		userob 		= UserOb.objects.get(user_id = request.user.id)
		questionob 	= QuestionOb.objects.order_by('-question_id')[0]
		answerOb	= AnswerOb.objects.order_by('answer_id')[0]

		an = datetime.datetime.now()

		k = an.minute - questionob.question_time.minute
		t = abs(k)
		
		context = {
			"user" 		: request.user,
			"userob"	: userob,
			"questionob": questionob,
			"answerOb"	: answerOb,
			"clock"		: t,
		}
		return render(request, "index.html", context)

@login_required
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/boa-admin/')

def settings_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/boa-admin/')
	else:
		success_f = False
		success_l = False
		success_m = False
		success_e = False
		success_c = False
		
		use 	= UserOb.objects.get(user_id = request.user.id)
		if request.method == 'POST' and 'personSave':
			firstname 	= request.POST['firstname']
			lastname	= request.POST['lastname']
			email		= request.POST['email']
			eduName		= request.POST['eduname']
			compName	= request.POST['compname']
			classNum	= request.POST['optionsRadiosInline']

			if firstname:
				request.user.first_name = firstname
				request.user.save()
				success_f = True

			if lastname:
				request.user.last_name = lastname
				request.user.save()
				success_l = True

			if email:
				request.user.email = email
				request.user.save()
				success_m = True
			if eduName:
				use.user_eduName = eduName
				use.save()
				success_e = True
			if compName:
				use.user_compName = compName
				use.save()
				success_c = True
			if classNum:
				use.user_eduClass = classNum
				use.save()

		context = {
			"user" 	    : request.user,
			"success_f"	: success_f,
			"success_l" : success_l,
			"success_m" : success_m,
			"success_e" : success_e,
			"success_c" : success_c,
			"user_ob"	: use,
		}
		return render(request, "settings.html", context)

def question_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/boa-admin/')
	else:
		question = QuestionOb.objects.all().order_by('-question_time')
		user 	 = UserOb.objects.all()

		context = {
			'question' : question,
			'userk'	   : user,
		}
		return render(request, "question_view.html", context)