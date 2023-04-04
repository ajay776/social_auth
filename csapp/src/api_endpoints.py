from .api_view import *
from django.urls import path

urlpatterns = [
       path("test", TestApiView.as_view())
]