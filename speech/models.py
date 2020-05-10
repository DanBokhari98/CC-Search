from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class History(models.Model):
    user_search = models.CharField(max_length = 1000)
    youtube_result = models.CharField(max_length = 1000)
    greeting = 'morning'
