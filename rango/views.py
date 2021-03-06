from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from models import *
from django.conf import settings
from rango.forms import *
from django.contrib import auth
from django.views.generic import *
from django.core import serializers
from serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.
import json

def index(request):
	context = RequestContext(request)
	category_list = Category.objects.all()
	print category_list
	context_dict = {'categories': category_list}
	return render_to_response('hello.html', context_dict, context)

def page(request):
        if request.method=='GET':
		cat=request.GET.get('category')	
        	context = RequestContext(request)
		if cat == 'food':
			page_list = Page.objects.filter(category_id=3)
                else:
			page_list = Page.objects.filter(category_id=4)		
        	context_dict = {'page': page_list}
        	return render_to_response('hello1.html', context_dict, context)



def about(request):

	txt="hi rango"+"<a href="+"/rango/>INDEX</a>"
	return HttpResponse(txt)

def about1(request):
	data=serializers.serialize('json',Category.objects.all())
	return HttpResponse(data, content_type="json")

	

def new(request):
	
	context=RequestContext(request)
	context_dict={"var":"god knows wat to do"}
        return render_to_response("hello.html",context_dict,context)

def new1(request):

        context_dict={"var":"god knows wat to do"}
        return render(request,"hello.html",context_dict)  



def search(request):
			
	return render(request,"search.html",{})


def search1(request):
	context = RequestContext(request)	
	err=False
	error=[];
	if request.method=='GET':
		
		if 'q' in request.GET:
			sea=request.GET.get('q')
		if not sea:
			err=True
			error.append('Enter a search term.')
		elif len(sea)< 3:
			err= True
			error.append('Please enter at most 20 characters.')
			print error
	if err == True:	
		error=error[0]	
		return render_to_response('search.html', {'error':error}, context)
	context_dict = {'value': sea}
        return render_to_response('search1.html', context_dict, context)





def contact(request):
	
	return render(request,"contact.html",{})


def contact1(request):
	
	context = RequestContext(request)
	err=False
	error=[];	
	if request.method=='POST':
		if 'name' in request.POST:
			name=request.POST.get('name')
		if 'email' in request.POST:
			email=request.POST.get('email')
		if 'message' in request.POST:
			query=request.POST.get('message')

		if not name:
			err=True
			error.append("please enter name")
		if not email or '@' not in email:
			err=True
			if not email:
				error.append("please enter email")
			else:
				error.append("please enter email correctly")
		if not query:
			err=True
			error.append("please enter message")
	if err == True:
		name=request.POST.get('name')
		email=request.POST.get('email')
		query=request.POST.get('message')
		return render_to_response('contact.html',{'error':error,'name':name,'email':email,'message':query}, context)
	fromemail=settings.EMAIL_HOST_USER;
	toemail=[email]
	
	send_mail(name,query,fromemail,toemail,fail_silently=False)	
	return HttpResponseRedirect('/rango/new1/')



def contacts(request):
	context = RequestContext(request)
	
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			fromemail=settings.EMAIL_HOST_USER;
        		if cd['email']:
				toemail=[cd['email'],]
			else:
				toemail=['noreply@example.com']
			name=cd['name']
			message=cd['message']
			send_mail(name,message,fromemail,toemail,fail_silently=False)
			return HttpResponseRedirect('/rango/new1/')
	else:
		form = ContactForm(initial={'message': 'I love your site!'})
	
	return render(request, 'contactform.html', {'form': form})		
	

def login(request):
	context = RequestContext(request)	
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			Username=cd['username']
			Password=cd['password']
			user = auth.authenticate(username=Username, password=Password)
			if user is not None:
				auth.login(request,user)
				return HttpResponseRedirect('/rango/new1/')
			else:
				return HttpResponseRedirect('/rango/login/')
	else:
		form=LoginForm();
	return render(request, 'loginform.html', {'form': form})

def searching(request):
	if request.method=="POST":
		form=SearchForm(request.POST)
		if form.is_valid():
			cd =form.cleaned_data
			sea=cd['search']
			if sea is not None:
				return HttpResponseRedirect("/rango/new1/")
			else:
				return HttpResponseRedirect("/rango/searching/")
	else:
		form=SearchForm();
	return render(request,"searching.html",{'form':form})

class StaticPage(TemplateView):
	template_name="searching.html"


def serialjson(request):

	if request.method=="POST":
		
		form=SearchForm(request.POST)
                if form.is_valid():
                        cd =form.cleaned_data
                        sea=cd['search']
                        if sea is not None:
				serial=PageSerializer(Page.objects.filter(title=sea),many=True)
				content=JSONRenderer().render(serial.data)
				content=json.loads(content)
				return HttpResponse(content[0]['id'])
	else:
		form=SearchForm();

		
	return render(request,"searching.html",{'form':form})	
