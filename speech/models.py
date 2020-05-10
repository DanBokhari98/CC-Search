from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class History(models.Model):
    user_search = models.CharField(max_length = 255)
    youtube_id = models.CharField(max_length = 255,blank=True)

    def set_youtube_result(self):
        #Do something with self.user_search
        self.youtube_id = 'l0U7SxXHkPY'
        self.save()
