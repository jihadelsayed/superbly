from urllib.parse import unquote
from menu.views import *
from messaging.views.messagesObj import *
from sgcommapp.models import *
from friends.views import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .services import SuperblyServices



class HomePageView(View):
    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        template_name = "home.html"

        user_obj = Profile.objects.filter(id=request.session['user_id'])
        friend_obj = Friends.objects.filter(user_id=request.session['user_id']).order_by('-id')
        message_obj = Messages.objects.filter(user_id=request.session['user_id']).order_by('-id')
        userIdOfSession = user_obj[0].username
        # username is equal to friendname in friends table
        friendObjId = Friends.objects.filter(friend_id=userIdOfSession)

        # Show Senders Messages
        senderObj = Messages.objects.filter(user_id=request.session['user_id']).order_by('-id')

        sndrMessageList = []
        for sndCntr in range(senderObj.count()):
            sndrMessageList.append(senderObj[sndCntr].message)

        # remove duplicates and return as a list
        sndrList = list(SuperblyServices.dedup(sndrMessageList, userIdOfSession, senderObj))

        # replaces sender name to "sent to all"
        sndr = SuperblyServices.rep_sender(sndrList, userIdOfSession)

        # extract urls from sent messages
        sentLinks, sentLinksUrls = SuperblyServices.extract_urls(sndr)
        sentLinksObj = dict(zip(sentLinks, sentLinksUrls))

        # Show Messages home.html
        msg = messagesObj(request)
        messageId, messageById = msg.getMessagesList(Messages)

        # extract urls from messages
        receivedLinks, receivedLinksUrls = SuperblyServices.extract_urls(messageById)
        receivedLinksObj = dict(zip(receivedLinks, receivedLinksUrls))

        # messageRowArray make a dictionary and store key:message number as checkbox name, value:message text
        messageRowsArray = dict(zip(messageId, messageById))

        # Show Saved Messages home.html
        msgSaved = messagesObj(request)
        savedMessagesList, savedMsgsSorted = msgSaved.getMessagesList(SavedMessages)

        # savedMessagesList.reverse()
        # extract urls from savedMessages
        savedLinks, savedLinksUrls = SuperblyServices.extract_urls(savedMsgsSorted)
        savedLinksObj = dict(zip(savedLinks, savedLinksUrls))


        data = {'username': request.session['username'], 'user': user_obj, 'friend': friend_obj,
            'message': message_obj, 'messagefrom': messageRowsArray, 'messageCount': messageId,
            'savedmessagefrom': savedMsgsSorted, 'senderFriend': sndr, 'receivedLinks': receivedLinksObj,
            'sentLinks': sentLinksObj, 'savedLinks': savedLinksObj }

        return render(request, template_name, data)
