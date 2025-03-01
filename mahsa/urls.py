from django.urls import path
from mahsa.views import *

urlpatterns = [
    path('' ,index_view),
    path('about' ,about_view),
    path('contact',contact_view)
]