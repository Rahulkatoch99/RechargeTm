from math import prod
from django.shortcuts import render
from .models import recharge
from .forms import recharge_form
import phonenumbers
from phonenumbers import carrier
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.




#detect povider

def operator(number):
    call='+91'+str(number)
    service_provider=phonenumbers.parse(call)
    return carrier.name_for_number(service_provider,'en')


#auto detect the provider

def carrier(request):
    if request.method=='POST':
        form=recharge_form(request.POST)
        # obj=recharge()
        # fm=optr(request.POST or None)
        if form.is_valid():
            number=request.POST['number']
            provider=operator(number)
            prod=request.POST['provider']
            form.save()
            messages.success(request,'recharge sucessfully...')
        return render(request,'home.html',{'form':form})
    else:
        form=recharge_form()
    return render(request,'home.html',{'form':form})
    # return render(request,'home.html',{'form':form})



    

    
   

def pro(request):
    if request.method=="GET":
        sm=recharge_form(request.GET)
        if sm.is_valid():
            number= request.GET['number']
            provider=request.GET['prod']
            
            # provider=operator(request)
            # pro=request.GET[provider]
            sm.save()
        return render(request, 'next.html', {'sm':sm})
    else:
        fm=recharge_form()
    return render(request,'next.html')
    

