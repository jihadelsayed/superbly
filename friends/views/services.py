from django.http import HttpResponseRedirect
from django.db.models import F
from sgcommapp.models import *



class SuperblyServices:
    def Test_User_Login(request):
        if 'user_id' not in request.session or 'username' not in request.session:
            return False
        else:
            return True

    def filter_messages(request, userFriends):
        # if user is a friend and added the user as a friend.
        friendIdFromObj = Friends.objects.filter(id=userFriends)
        userIdFromObj = Profile.objects.filter(username=friendIdFromObj[0].friend_id)
        friendIdObj = Friends.objects.filter(user_id=userIdFromObj[0].id, friend_id=request.session['username'])

        return friendIdObj
