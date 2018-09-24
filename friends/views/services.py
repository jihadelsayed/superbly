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
        noFriendId = False
        # if user is a friend and added the user as a friend.
        friendIdFromObj = Friends.objects.filter(id=userFriends)
        if len(friendIdFromObj) > 0:
            userIdFromObj = Profile.objects.filter(username=friendIdFromObj[0].friend_id)
            friendIdObj = Friends.objects.filter(user_id=userIdFromObj[0].id, friend_added='True', friend_id=request.session['username'])

            return friendIdObj
        else:
            return noFriendId

    def notify_user(request, userid, added):
        if added:
            messageObj = " wants to talk with you."
        else:
            messageObj = " removed you."

        notifyObj = Notifications(user_id=userid, friend_id = request.session['username']  ,message=messageObj)
        notifyObj.save()
