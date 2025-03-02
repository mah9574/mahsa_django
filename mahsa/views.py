from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'mahsa/index.html')

def about_view(request):
    return render(request,'mahsa/about.html')

def contact_view(request):
    return render(request,'mahsa/contact.html')


