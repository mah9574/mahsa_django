from django.urls import path
from mahsa.views import *

app_name = 'mahsa'

urlpatterns = [
    path('' ,index_view, name ='index'),
    path('about' ,about_view, name ='about'),
    path('contact',contact_view, name ='contact'),
    path('test',test_view, name ='test')
]