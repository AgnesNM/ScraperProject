from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
import requests

from . models import Tshirt
from django.db.models import Count, Min, Max, Sum, Case, When, F, Value, IntegerField

#from ScraperApp import forms
from . forms import ScraperInput
from . models import Scrapers

from django.db import connection


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

def slack_integration(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    
    slack_dict = {'insert_me': users}
    return render (request, 'ScraperApp/index.html', context = slack_dict)


def raw_sql(request):

    print("hey")
    for p in Tshirt.objects.raw("SELECT * FROM ScraperApp_tshirt"):
        print("hello")
        print(p)      


def data(request):

    # sizes = Tshirt.objects.count()

    # total = Tshirt.objects.aggregate(total=Count("tshirt_id"))

    # print(f"the total number of tshirts is {total}")

    # print(f"The total number of tshirts is {sizes}")

    # sizes_2 = Tshirt.objects.filter(size="small").count()

    small_tshirt_count = Tshirt.objects.filter(size='small').aggregate(total_count=Count('id'))
    
    print(small_tshirt_count)

    print(f"The total number of small sized tshirts is {small_tshirt_count}")

    # sizes_3 = Tshirt.objects.values('size').annotate(count=Count('size'))

    sizes_dict = {"size": small_tshirt_count}

    return render(request, "ScraperApp/data.html", context = sizes_dict)


# num_posts = Post.objects.aggregate(num_posts=Count('id'))
# print(num_posts)

# def home(request):
#     my_dict = {"insert_me": "Welcome to SuperScraper. On what site do you want to scrape?" }
#     return render( request, "ScraperApp/index.html", context = my_dict) 


def minimum(request):

    min_price = Tshirt.objects.aggregate(least_priced=Min("price"))

    # min_price = Tshirt.objects.filter(color="red").aggregate(Min("price"))

    # min_price = Tshirt.objects.aggregate(Min("price")).filter(color="white")

    print(min_price)

    min_price_decimal = min_price["least_priced"]
    min_price_float = float(min_price_decimal)

    print(f"The cheapest tshirt in our database is: {min_price_float}")


    # min_price = Tshirt.objects.annotate(Min("price"))

    min_price_dict = {"min_price": min_price}

    return render(request, "ScraperApp/minimum.html", context = min_price_dict)


def maximum(request):

    max_price = Tshirt.objects.aggregate(most_priced=Max("price"))

    print(max_price)

    max_price_decimal = max_price["most_priced"]
    max_price_float = float(max_price_decimal)

    print(f"The most expensive tshirt in our database is: {max_price_float}")

    # min_price = Tshirt.objects.annotate(Min("price"))

    max_price_dict = {"max_price": max_price}

    return render(request, "ScraperApp/maximum.html", context = max_price_dict)

def sum(request):

    total_value = Tshirt.objects.aggregate(total_val=Sum("price"))

    print(total_value)

    total_value_decimal = total_value["total_val"]
    total_value_float = float(total_value_decimal)

    print(f"The total value of tshirts in our database is: {total_value_float}")

    total_value_dict = {"total_val": total_value}


    return render(request, "ScraperApp/sum.html", context = total_value_dict)

def defective(request):

    total_value = Tshirt.objects.aggregate( 
    
        tshirts_value=Sum(
            Case(
                When(defective=False, then=F("price")),
                default=Value(0),
                output_field=IntegerField(),
            )
        )
    )

    print(f"The total value of non-defective tshirts is {total_value['tshirts_value']}")

    defective_dict = {"defective": total_value}

    return render(request, "ScraperApp/defective.html", context = defective_dict)

 

def manual(request):
    
    all_tshirts = Tshirt.objects.all()

