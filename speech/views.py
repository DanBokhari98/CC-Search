from django import urls
from django.views.generic import CreateView,DetailView
from speech.models import History

class HistoryCreate(CreateView):
    model = History
    template_name = 'splash.html'
    fields = [
        'user_search',
    ]

    def form_valid(self,form):
        result = super().form_valid(form)
        self.object.set_youtube_result()
        return result

    def get_success_url(self):
        return urls.reverse("success",kwargs = {'pk':self.object.id})


class Success(DetailView):
    template_name = "success.html"
    model = History
