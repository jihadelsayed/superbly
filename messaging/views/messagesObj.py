from sgcommapp.models import *


class messagesObj():
    def __init__(self, req):
        self.MsgsList = []
        self.req = req
        self.messageID = []

    def getMessagesList(self, MessagesObj):
        Messages = MessagesObj.objects.all().order_by('-id')
        for messages in Messages:
            friend = Friends.objects.filter(id=messages.friend_id)
            user = Profile.objects.filter(username=friend[0].friend_id)
            if messages.user_id == int(friend[0].user_id) and self.req.session['user_id'] == user[0].id:
                messageSender = Profile.objects.filter(id=messages.user_id)
                if messageSender:
                    self.MsgsList.append(messages.message + " | " + messageSender[0].username)
                    # print(messages.id)
                    self.messageID.append(messages.id)

        # MsgsSorted = sorted(self.MsgsList, reverse=True)
        MsgsSorted = self.MsgsList
        return self.messageID, MsgsSorted

    def deleteAllMessages(self, MessagesObject):
        user_obj = Profile.objects.filter(id=self.req.session['user_id'])
        friend_obj = Friends.objects.filter(user_id=self.req.session['user_id']).order_by('-id')
        message_obj = MessagesObject.objects.filter(user_id=self.req.session['user_id']).order_by('-id')
        userIdOfSession = user_obj[0].username
        # username is equal to friendname in friends table
        friendObjId = Friends.objects.filter(friend_id=userIdOfSession)
        if friendObjId.count():
            getId = friendObjId
            cntr = 0
            messageIdFromFriend = []
            # messageIdFromUser = []
            for message in friendObjId:
                # friend id in messages is equal to id in friends table
                messageFriendIdObj = MessagesObject.objects.filter(friend_id=friendObjId[cntr].id).order_by('-id')
                for messageFromFriend in messageFriendIdObj:
                    messageIdFromFriend.append(int(messageFromFriend.id))  #:
                cntr = cntr + 1
            messageSorted = sorted(messageIdFromFriend, reverse=True)
            # print(messageSorted)
            # messageSortedById = []
            for messageSort in messageSorted:
                MessagesObject.objects.get(id=messageSort).delete()

        # Delete My Messages
        MessagesObject.objects.filter(user_id=self.req.session['user_id']).delete()

    def getFriendObj(self):
        userMessages = Profile.objects.filter(id=self.req.session['user_id'])
        # print(userMessages) #request.session['user_id'] = 7 userMessages[0] = jun
        friendMessages = Friends.objects.filter(friend_id=userMessages[0])

        return friendMessages
