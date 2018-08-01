from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from sgcommapp.models import *
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import View
from .services import SuperblyServices

class DeleteFriend(View):


    def get(self, request, friend_id):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
        #remove friend if delete button is clicked.
        Friends.objects.get(id=friend_id).delete()
        return HttpResponseRedirect('/home')
