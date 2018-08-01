from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect

from sgcommapp.models import *
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import View

from .services import SuperblyServices

import urllib

class MessageFriend(View):

    def send_to_all(request, friend_id):
        message = request.POST.get('message')
        friendIdFromGet = request.POST.get('id')  # friends id
        user = request.session['user_id']
        msgCheckBox = request.POST  # get if the checkboxes are checked.
        friendsNotAddedList = []
        userFriendsObj = Friends.objects.filter(user_id=user)
        cntr = 0
        if message:
            if "sendtoall" in msgCheckBox:  # if checkbox with name sendtoall is checked
                for userFriends in userFriendsObj:  # iterate to all user's friends
                    friendIdObj = SuperblyServices.filter_messages(request, userFriends.id)

                    if friendIdObj.count():
                        message_obj = Messages(message=request.POST.get('message'), user_id=user, friend_id=userFriends.id)
                        message_obj.save()
                        cntr = cntr + 1
                    else:
                        friendsNotAddedList.append(userFriends.friend_id)
                if len(friendsNotAddedList) > 0:
                    if cntr == 0:
                        return "<script>alert('Message is not sent to anyone. No one has added you yet. ');window.location = '/'</script>"
                    else:
                        friendsNotSent = ""
                        for friends in friendsNotAddedList:
                            friendsNotSent = friendsNotSent + friends + ", "

                        return "<script>alert('Message is sent to " + str(cntr) + " except: " + friendsNotSent + "');window.location = '/'</script>"
                else:
                    #increment 1 to Stats number messages sent
                    #SuperblyServices.increment_msgs_sent(request)

                    return "<script>alert('Message is sent to all');window.location = '/home'</script>"
            else:
                # send message to only one user.
                friendIdObj = SuperblyServices.filter_messages(request, friendIdFromGet)

                if friendIdObj.count():
                    message_obj = Messages(message=request.POST.get('message'), user_id=user,
                                           friend_id=request.POST.get('id'))
                    message_obj.save()
                    #increment 1 to Stats number messages sent
                    #SuperblyServices.increment_msgs_sent(request)

                    return "<script>alert('Message is sent.');window.location = '/home'</script>"
                else:
                    return "<script>alert('Your friend has not added you yet.');window.location = '/home'</script>"
        else:
            return "<script>alert('Message is empty.');window.location = '/home'</script>"

    def get(self, request, friend_id):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        data = {'username': request.session['username'], 'friend': friend_id}
        return render(request, 'message_friend.html', data)

    def post(self, request, friend_id):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        friendsMessageStr = MessageFriend.send_to_all(request, friend_id)

        return HttpResponse(friendsMessageStr)
