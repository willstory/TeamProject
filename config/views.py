from django.urls import reverse_lazy
from django.views import generic
from member.forms import MemberCreationForm  # 커스텀 사용자 모델을 위한 폼

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = MemberCreationForm  # 수정된 부분
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(generic.TemplateView):
    template_name = 'registration/register_done.html'