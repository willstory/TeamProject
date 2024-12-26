from django.views.generic import TemplateView

# 메인 페이지
class Homeview(TemplateView):
    template_name = 'home.html'  # 템플릿 파일명
