from django.urls import path 
from . import views


urlpatterns = [
    path('',views.main, name= "home"),
    path('enquiry',views.enquiry, name= "enquiry"),
    path('feedback',views.feedback,name='feedback')
]