from django.shortcuts import render, get_object_or_404
import json	
from django.http import Http404
import json
# import requests
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .models import Contact
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def resume(request):
    r_user = request.user
    
    if request.method == "POST":
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if Contact.objects.filter(message=message).exists():
            return JsonResponse("<p class='alert alert-danger text-center' style=''>{} you have already sent this message<p>".format(name), safe=False)
        else:
            contact = Contact(name=name,email = email, message = message)
            contact.save()

            return JsonResponse("<p class='alert alert-success text-center' style=''>{} Thanks for contacting me, I will reach out to you soon<p><script>window.location.href = './';</script>".format(name), safe=False)
    return render(request, "dev/index.html")