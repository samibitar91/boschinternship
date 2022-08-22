from django.shortcuts import render
from django.http import HttpResponse

"""
this view makes HTTP response for the home page
"""

def home (request): 

    return render(request, 'index.html')
