from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from sgcommapp.models import *
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import View
from .services import SuperblyServices

class AddFriend(View):


    def get(self, request, *args, **kwargs):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
        template_name = 'home.html'
        data = {'username': request.session['username']}
        return render(request, template_name, data)


    def post(self, request, *args, **kwargs):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
            
        friendName = request.POST.get('friend')
        userNameId = request.session['user_id']
        userNameObj = Profile.objects.filter(id=userNameId)
        user_obj = Profile.objects.filter(username=request.POST.get('friend'))
        if userNameObj[0].username != friendName:
            if user_obj.count():
                friendAddedObj = Friends.objects.filter(friend_id=friendName, friend_added='True', user_id=userNameId)
                if not friendAddedObj:
                    friend_obj = Friends(friend_id=request.POST.get('friend'), user_id=request.session['user_id'],
                                         friend_added=True)
                    friend_obj.save()

        return HttpResponseRedirect('/home')
