from django.shortcuts import render

# Create your views here.
def academy_list(request):
    return render(request, 'academy_list.html')