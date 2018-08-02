from sgcommapp.models import *


class messagesObj():
    def __init__(self, req):
        self.MsgsList = []
        self.req = req
        self.messageID = []

    def getMessagesList(self, MessagesObj):
        #Gets the profile username
        userIdObj = Profile.objects.filter(id = self.req.session['user_id'])
        #Gets all messages sent to the username logged in. Show latest first.
        Messages = MessagesObj.objects.filter(friend__friend_id = userIdObj[0].username).order_by('-id')
        for messages in Messages:
            messageSender = Profile.objects.filter(id = messages.user_id)
            if messageSender:
                self.MsgsList.append(messages.message + " | " + messageSender[0].username)
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
