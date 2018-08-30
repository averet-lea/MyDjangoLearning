from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord,Topic,Webpage,user
from AppTwo.forms import FormName,FormUser
# Create your views here.

def index(request):
    context_dict = {'text':'some text','number':1234567}
    return render(request,'AppTwo/index.html',context=context_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'AppTwo/help.html',context=helpdict)

def users(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            print("VALID data!")
            print("Name: "+form.cleaned_data['first_name'])
            print("Email: "+form.cleaned_data['last_name'])
            print("Text: "+form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR ADDING USER')
    return render(request,'AppTwo/users.html',{'form':form})


def form_name_view(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print("VALID data!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request,'AppTwo/form_name.html',{'form':form})

def other(request):
    return render(request,'AppTwo/other.html')

def url_templates(request):
    return render(request,'AppTwo/url_templates.html')

def base(request):
    return render(request,'AppTwo/base.html')
