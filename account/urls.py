from django.urls import path

from . import views

urlpatterns = [
    path('',views.signin, name='signin'),
    path('register',views.register, name='register'),
    path('signout',views.signout, name='signout')
    
]