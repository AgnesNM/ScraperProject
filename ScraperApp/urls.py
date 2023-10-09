from django.urls import path

from ScraperApp import views

urlpatterns = [
    # path("", views.scraper, name = "scraper"),   
    path("", views.slack_integration, name = "slack_integration"), 
    path("data/", views.data, name = "data"), 
    path("minimum/", views.minimum, name = "minimum"),
    path("maximum/", views.maximum, name = "maximum"), 
    path("sum/", views.sum, name = "sum"),
    path("defective/", views.defective, name = "defective"),
    path("raw_sql/", views.raw_sql, name = "raw_sql"),            
]