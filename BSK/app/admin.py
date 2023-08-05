from django.contrib import admin
from .models import *

models_list = [Vacancy, Subscriber, Tender, News, User, Lot, Statistics, Application, Service, Contact, Leader]

for model in models_list:
    admin.site.register(model)
