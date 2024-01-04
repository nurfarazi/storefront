from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the playground index.")
def get_html(request):
    return render(request, 'index.html')