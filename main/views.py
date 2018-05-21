from django.views.generic.base import TemplateView


# Create your views here.

class MainPageView(TemplateView):
    template_name = 'mainpage.html'
