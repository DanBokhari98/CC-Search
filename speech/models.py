from django.db import models

class History(models.Model):
    user_search = models.CharField(max_length = 1000)
    youtube_result = models.CharField(max_length = 1000)
    greeting = 'morning'
