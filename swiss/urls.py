from django.urls import path
from . import views     
"""
namespacing URLs in swiss
"""
urlpatterns=[
    path('/swiss/index/', views.home)
]