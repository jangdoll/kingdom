from django.shortcuts import render
from django.views import View


def main_page(request):
    return render(request, 'index.html')
