from django.http import HttpResponseRedirect
from django.views.generic import View
from messaging.views.messagesObj import *

from django.http import HttpResponse
from sgcommapp.models import *

from .services import SuperblyServices


class DeleteSavedMessages(View):
    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        msg = MessagesObj(request)
        msg.deleteAllMessages(SavedMessages)
        return HttpResponseRedirect('/home')

    def post(self, request):
        pass
