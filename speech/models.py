from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from youtube_search import YoutubeSearch as Ys
from youtube_transcript_api import YouTubeTranscriptApi as Yta
import json, math

class History(models.Model):
    user_search = models.CharField(max_length = 255)
    youtube_id = models.CharField(max_length = 255,blank=True)
    youtube_time = models.CharField(max_length = 255, default="0")

    def set_youtube_result(self):
        cc_search = self.user_search
        word = cc_search.lower()
        cc_search = '"' + cc_search + '", cc'

        results = Ys(cc_search, max_results=5).to_json()
        result_dict = json.loads(results)

        self.youtube_id = result_dict["videos"][0]["id"]
        transcript = Yta.get_transcript(self.youtube_id)
        #print(type(transcript))
        if transcript is not None:
            self.set_youtube_time(word, transcript)

        self.save()

    def set_youtube_time(self, word, transcript):
        time = 0
        for i in range(len(transcript)):
            if word in transcript[i]['text'].lower():
                time = transcript[i]['start']
                break
        self.youtube_time = int(time)
