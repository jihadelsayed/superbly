from django.http import HttpResponseRedirect
from django.views.generic import View
from messaging.views.messagesObj import *
from django.shortcuts import render
from django.http import HttpResponse
from sgcommapp.models import *

from .services import SuperblyServices


class DeleteMessage(View):
    def get(self, request, user_message):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")


        template_name = 'delete_message.html'

        userName = request.session['username']

        message = user_message.replace('forward_slash', '/')

        variables = {'username': userName,'current_message': message}
        return render(request, template_name, variables)

    def post(self, request, user_message):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        userName = request.session['username']

        userObj = Profile.objects.filter(username=userName)
        message = request.POST.get('currentmessage')
        message_only = message.split("|")
        #sender_only = message_only[1].split("to")
        try:
            messageObj = Messages.objects.filter(user_id=userObj[0].id, message=message_only[0].strip())

            if len(messageObj) > 0:
                messageObj.delete()

                return HttpResponse("<script>alert('Message Deleted.');window.location = '/home'</script>")
            else:
                return HttpResponse("<script>alert('Cannot Delete Message.');window.location = '/home'</script>")
        except:

            return HttpResponse("<script>alert('Cannot Delete Message.');window.location = '/home'</script>")
