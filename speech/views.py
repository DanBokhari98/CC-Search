from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

class History(CreateView):
    #model = models.History
    user_search = models.CharField(max_length = 1000)
    youtube_result = models.CharField(max_length = 1000)
    greeting = 'morning'
    template_dir = "splash.html"
