from django.views import generic

class Homeview(generic.TemplateView):
    template_name='home.html'