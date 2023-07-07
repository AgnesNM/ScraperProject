from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


#from ScraperApp import forms
from . forms import ScraperInput
from . models import Scrapers

# Create your views here.  

def form_view(request):

    # if this is a POST request we need to process the form data

    if request.method == "POST":

        # create a form instance and populate it with data from the request:

        form = ScraperInput(request.POST)

        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # print(form.cleaned_data["username"])
            # print(form.cleaned_data["email"])       

            data = form.cleaned_data

            #create a new instance of the model

            user_info = Scrapers(email = data["email"], username = data["username"])
            
            #save the instance to the database

            user_info.save()

            HttpResponseRedirect("/thanks/") #redirect to sso?
            

    # if a GET (or any other method) we'll create a blank form
    
    else:

        form = ScraperInput()

    return render(request, "ScraperApp/index.html", {"form": form})
   

def scraper(request):
    return HttpResponse("Hey, this is another view in the Scraper App.")

# def home(request):
#     my_dict = {"insert_me": "Welcome to SuperScraper. On what site do you want to scrape?" }
#     return render( request, "ScraperApp/index.html", context = my_dict) 