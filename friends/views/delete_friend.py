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
        userName = request.session['username']
        friendNameObj = Friends.objects.filter(id=friend_id)
        userObj = Profile.objects.filter(username = friendNameObj[0].friend_id)
        friendAddedObj = Friends.objects.filter(user_id = userObj[0].id, friend_added = 'False')
        friendExistObj = Friends.objects.filter(user_id = userObj[0].id, friend_id = userName)

        if friendAddedObj or not friendExistObj:
            Friends.objects.get(id=friend_id).delete()
            added = False
            SuperblyServices.notify_user(userObj[0].id, request.session['username'], added)
        else:
            Friends.objects.filter(id = friend_id).update(friend_added = 'False')
            added = False
            SuperblyServices.notify_user(userObj[0].id, request.session['username'], added)

        # 08/24/2018 --end--
        return HttpResponseRedirect('/home')
