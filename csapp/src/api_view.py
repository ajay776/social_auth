from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import authentication, permissions
# from  rest_framework import P
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import * 



class TestApiView( APIView):
       authentication_classes = [TokenAuthentication ]
       # permission_classes = [AllowAny]
       def get(self, request):
              import pdb;pdb.set_trace()
              return Response("completed Request")