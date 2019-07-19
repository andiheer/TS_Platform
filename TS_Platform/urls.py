"""
Definition of urls for TS_Platform.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from userlogin import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/',views.register, name='register'),
    path('login/',
         LoginView.as_view
         (
             template_name='userlogin/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('offer/',views.add_offer,name='offer'),
    path('profile/',views.profile, name='profile'),
    path('view_offers',views.view_offers, name='view_offers'),
    path('details/<int:offer_id>/',views.offer_details,name='details'),
    path('admin/', admin.site.urls),
]
