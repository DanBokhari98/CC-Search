from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from speech.models import models
from speech.models import History

class HistoryCreate(CreateView):
    model = History
    fields = ['name']
    template_dir = 'splash.html'
    user_search = models.CharField(max_length = 1000)
    youtube_result = models.CharField(max_length = 1000)
    greeting = 'morning'

    def get(self, request, *args, **kwargs):
#        users = User.objects.all()
        return render(request, 'splash.html')


    def history(request):
        #return HttpResponse('History')
        return render(request, 'splash.html')
