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

        added = False

        if userNameObj[0].username != friendName:
            if user_obj.count():
                friendAddedObj = Friends.objects.filter(friend_id=friendName, friend_added='False', user_id=userNameId)
                if friendAddedObj:
                    friendUserIDObj = Friends.objects.filter(friend_id = request.session['username'], user_id = user_obj[0].id)
                    if friendUserIDObj:
                        #if the user is existing in the Friends database, make friend_added as True.
                        Friends.objects.filter(friend_id = friendName).update(friend_added = 'True')

                        added = True
                        SuperblyServices.notify_user(request, user_obj[0].id, added)
                else:
                    #if the user in Friends database has friend_added = False with user_id of the friend
                    friendUserIDObj = Friends.objects.filter(friend_id = request.session['username'], friend_added = 'False', user_id = user_obj[0].id)
                    if friendUserIDObj:
                        #if user in Friend db has friend_added = True
                        friendObj = Friends.objects.filter(friend_id=friendName, friend_added='True', user_id=userNameId)
                        if not friendObj:
                            friend_obj = Friends(friend_id=request.POST.get('friend'), user_id=request.session['user_id'],
                                                 friend_added=True)
                            friend_obj.save()
                            Friends.objects.filter(friend_id = request.session['username'], user_id = user_obj[0].id).update(friend_added = 'True')

                            added = True
                            SuperblyServices.notify_user(request, user_obj[0].id, added)

                    else:
                        friendObj = Friends.objects.filter(friend_id=friendName, friend_added='True', user_id=userNameId)
                        if not friendObj:
                            #if the user is not existing in the Friends database, add the user in the db and friends list.
                            friend_obj = Friends(friend_id=request.POST.get('friend'), user_id=request.session['user_id'],
                                                 friend_added=False)
                            friend_obj.save()

                            added = True
                            SuperblyServices.notify_user(request, user_obj[0].id, added)

        return HttpResponseRedirect('/home')
