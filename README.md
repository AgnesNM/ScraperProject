# The Web Scraping Project
The goal of this web scraping project is to create a web scraping tool that works within communities like Slack, Discord, and even private product communities, to pick up conversations based on set keywords and put them in a way that is easy for someone to have them in one place, for example, a CSV file. The tool should also be able to rank the chats based on criteria like the number of replies and the number of times asked.

# Implementation
The project could be implemented like a Slack and Discord Integration. It could be a Chrome extension or a SaaS. We'll attempt the SaaS integration.


#### 13th September 2022

## Setup/Installation Requirements

We shall use a [Product Requirements Document on Confluence](https://webscrape.atlassian.net/l/cp/vqeHskyJ) to layout project requirements, and map out details like the roadmap, and supportive diagrams

### Set up your coding environment

#### Technologies 

- Django (we used v4.1.3)
- Beautiful Soup (we shall use the **lxml** library)
- the **requests** library
- the **bs4** library that stands for Beautiful Soup V4
- Deploy to AWS using an **Amazon EC2 instance** (to be confirmed)


#### Backend set up
- Install anaconda navigator.
- Create a virtual environment within Conda or activate one if you already have some envs.
- Install the above libraries (Beautiful Soup, requests, and bs4) via pip or conda.

##### Django set up
- Create a virtual environment 
- Install Django via pip or conda (use `python -m django --version` or `django-admin --version` to check if it's already installed)
- Create a Django project (the root directory should house manage.py and is your project's container). Our  project's root directory in this case is 'ScraperProject', and it houses manage.py.
- Use the following command to create a project:
`django-admin startproject ScraperProject`
- Our actual Python package is also called 'ScraperProject' and houses the rest of the project files.
- To verify that your Django project works, run the following command (make sure your working directory is the one housing the project's manage.py):
        `python manage.py runserver` 
- Create an app. Ensure that you are in the same directory as manage.py. Our app directory is called 'ScraperApp'.
- Use the following command to create an app:
`python manage.py startapp ScraperApp`


###### Project settings
- In our project's settings.py module we need to notify Django that we have added another app, 'ScraperApp'. We'll add our app to the 'INSTALLED_APPS' list

- Check that your server still runs properly after the changes. Run `python manage.py runserver` again.


###### App Views
- Add a single sign on view. We'll use the django-simple-sso library. 



##### Dependencies


##### Running the server



###### Running the endpoints


#### Database



##### Database setup


#### Frontend setup

