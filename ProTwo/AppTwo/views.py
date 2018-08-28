from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord,Topic,Webpage,user
from AppTwo.forms import FormName,FormUser
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'AppTwo/index.html',context=date_dict)

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
