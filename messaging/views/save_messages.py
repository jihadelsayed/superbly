from django.http import HttpResponseRedirect
from django.views.generic import View
from messaging.views.messagesObj import *

from django.http import HttpResponse
from sgcommapp.models import *

from .services import SuperblyServices


class SaveMessages(View):
    def get(self, request):
        pass

    def post(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        # userMessages = User.objects.filter(id=request.session['user_id'])
        # #print(userMessages) #request.session['user_id'] = 7 userMessages[0] = jun
        # friendMessages = Friends.objects.filter(friend_id=userMessages[0])

        friendMsgObj = MessagesObj(request)
        friendMessages = friendMsgObj.getFriendObj()

        messageId = request.POST  # get SaveCheckedMessages form and if the checkboxes are checked.
        id = []

        for message in friendMessages:
            idMessages = Messages.objects.filter(friend_id=message.id)  # search if jun has a message
            if idMessages.count() > 0:
                for msg in idMessages:
                    # print(msg.id) #85
                    if str(msg.id) in messageId:  # check if checkboxes are checked then append to list
                        id.append(str(msg.id))  # get the message id

        for messagesId in id:
            savedMessagesObj = Messages.objects.filter(id=messagesId)
            savedMsgExist = SavedMessages.objects.filter(user_id=savedMessagesObj[0].user_id,
                                                         friend_id=savedMessagesObj[0].friend_id,
                                                         message=savedMessagesObj[0].message)
            # check if messages are already saved or exist.
            if savedMsgExist.count() < 1:
                savedMessages = SavedMessages(user_id=savedMessagesObj[0].user_id,
                                              friend_id=savedMessagesObj[0].friend_id,
                                              message=savedMessagesObj[0].message)
                savedMessages.save()

        return HttpResponseRedirect('/home')
