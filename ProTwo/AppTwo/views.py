from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord,Topic,Webpage,user
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'AppTwo/index.html',context=date_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'AppTwo/help.html',context=helpdict)

def users(request):
    userlist = user.objects.order_by('first_name')
    user_dict = {'user_list':userlist}
    return render(request,'AppTwo/users.html',user_dict)
