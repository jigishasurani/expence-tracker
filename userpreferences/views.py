from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
# Create your views here.

def index(request):

    currency_data = []

    file_path = os.path.join(settings.BASE_DIR,'currencies.json')

    with open(file_path,'r') as json_file:

        data = json.load(json_file)

        for k,v in data.items():
            currency_data.append({'name':k,'value':v})


    exists=UserPreferences.objects.filter(user=request.user).exists()
    user_preferences = None
    
    if exists:
       user_preferences= UserPreferences.objects.get(user=request.user)

    if request.method=='GET':
        

    #import pdb
    #pdb.set_trace()

        return render(request, 'preferences/index.html',{'currencies' : currency_data, 'user_preferences' : user_preferences})

    
    else:
        currency = request.POST.get('currency')

        if exists:
            
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreferences.objects.create(user=request.user,currency=currency)
        messages.success(request, 'Changes Saved')

        return render(request, 'preferences/index.html',{'currencies' : currency_data,'user_preferences' :user_preferences})