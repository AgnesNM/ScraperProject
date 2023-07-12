from django.urls import path

from ScraperApp import views

urlpatterns = [
    # path("", views.scraper, name = "scraper"),   
    path("", views.slack_integration, name = "slack_integration"),    
]