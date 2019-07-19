"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import addOfferForm
from .models import offers, offeringType

# Import custom register form
from userlogin.forms import RegisterForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    # Is user authenticated? If yes, send him to the profile view
    # If not, to the Home page

    if request.user.is_authenticated:
        return redirect(profile)
    
    else:
        return render(
            request,
            'userlogin/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'userlogin/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'userlogin/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def profile(request):
    """Renders the profile page """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'userlogin/profile.html',
        {
            'title' : 'Profile',
            'year':datetime.now().year,
        }
        
    )

def register(request):
    """ Renders register form."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'userlogin/register.html', 
                  {
                      'title':'Register',
                      'year':datetime.now().year,
                      'form': form,
                      
                    }
                  )

def add_offer(request):
    """ Renders offering form """
    # Check if user is logged in
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = addOfferForm(request.POST)
            if form.is_valid():
                all_form=form.save(commit=False)
                all_form.id_user=request.user
                # Initialize offering state: 0 = open
                all_form.offering_state = 0
                form.save()
                return redirect('profile')

        else:
            # Print out form
            form = addOfferForm()
            return render(request, 'userlogin/add_offer.html',
                            {
                                'title':'Add your offer',
                                'year':datetime.now().year,
                                'form': form,
                                'errormessage':'Please log in',
                            
                            }
                          )
    # If user is not authenticated, redirect to home
    else:
        return redirect('home')

def view_offers(request):
    """ Lists offerings """
    # Check if user is logged in
    if request.user.is_authenticated:
        # offers_query = offers.objects.all()
        # current_user = request.user
        # user_id = current_user.id
        offers_query = offers.objects.exclude(id_user_id=request.user.id)
        # context = {'offers_query': offers_query}
        return render(request, 'userlogin/view_offers.html',
                        {
                            'title': 'All offers',
                            'year': datetime.now().year,
                            'offers_query': offers_query,
                            'errormessage':'Please log in',
                        }
                     )
    # If user is not authenticated, redirect to home
    else:
        return redirect('home')

def offer_details(request,offer_id):
    """ List offering and allow to select offer """
    # Check if user is logged in
    if request.user.is_authenticated:
        return HttpResponse("You're looking at offer %s." % offer_id)

    # If user is not authenticated, redirect to home
    else:
        return redirect('home')




    

