from sgcommapp.models import *
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from random import randint

from .services import SuperblyServices
from .profile import ProfileObj

import time
import datetime

class LoginView(View):

    def get(self, request, user, password):
        #Account lock removal
        messageObj = " unlocked your account. Did you try to unlock your account on " +  str(datetime.datetime.now()) + "? If not, change your password, then logout and login."
        userObj = Profile.objects.filter(username = user, password = password)
        if userObj:
            notifyObj = SuperblyServices.notify_user(userObj[0].id, user, messageObj)
            time.sleep(60)#1 minute
            #update account locked to false
            Account.objects.filter(username=user).update(logged = False)
            return HttpResponse("<script>alert('Account is open. You may log-in.');window.location = '/';</script>")
        else:
            return HttpResponse("<script>alert('You cannot unlock this account.');window.location = '/';</script>")

    def post(self, request):
        #get hashed password
        profile = ProfileObj(request)
        hashed_password = profile.replacePassword()

        user_obj = Profile.objects.filter(username=request.POST.get('username'), password=hashed_password)
        if user_obj.count():
            accountObj = Account.objects.filter(username = request.POST.get('username'), logged = 'True')
            if not accountObj:
                #create session cookies
                user_id, username = profile.createSession(user_obj[0])

                accountExistObj = Account.objects.filter(username = request.POST.get('username'))
                if accountExistObj:
                    Account.objects.filter(username=username).update(logged = True)
                    #notification time and date
                    messageObj = " logged-in on: " + str(datetime.datetime.now())
                    notifyObj = SuperblyServices.notify_user(user_id, username, messageObj)
                else:
                    createAccount = Account(id=user_id,username=username, password=hashed_password, logged = True)
                    createAccount.save()
            else:
                return HttpResponse("<script>alert('Account is locked. Please press logout when logging out. Click OK and wait for 1 minute then log in.');window.location = '/account-locked/" + request.POST.get('username') + "/" + hashed_password + "'; </script>")

        return HttpResponseRedirect('/home')
