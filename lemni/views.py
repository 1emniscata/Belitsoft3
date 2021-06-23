from django.shortcuts import render
from django.views.generic.base import View



def main(request):
    return render(request, 'lemni/base.html')



