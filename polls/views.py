from django.http import request
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'polls/index.html')
def about(request):
    return render(request, 'polls/about.html')
def contact(request):
    return render(request, 'polls/contact.html')
def single_page(request):
    return render(request, 'polls/single_page.html')