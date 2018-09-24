from sgcommapp.models import *
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from random import randint

from .services import SuperblyServices

import time
import datetime

class LoginView(View):

    def get(self, request, user):
        #Account lock removal
        messageObj = " unlocked your account. Did you try to unlock your account on " +  str(datetime.datetime.now()) + "? If not, change your password, then logout and login."
        userObj = Profile.objects.filter(username = user)
        notifyObj = Notifications(user_id = userObj[0].id , friend_id = user, message=messageObj)
        notifyObj.save()
        time.sleep(60)#1 minute
        Account.objects.filter(username=user).update(logged = False)
        return HttpResponse("<script>alert('Account is open. You may log-in.');window.location = '/';</script>")

    def post(self, request):
        plain_password = request.POST.get('password')
        hashed_password = SuperblyServices.hash_pass(plain_password)

        user_obj = Profile.objects.filter(username=request.POST.get('username'), password=hashed_password)
        if user_obj.count():
            accountObj = Account.objects.filter(username = request.POST.get('username'), logged = 'True')
            if not accountObj:
                request.session['user_id'] = user_obj[0].id
                request.session['username'] = user_obj[0].username
                accountExistObj = Account.objects.filter(username = request.POST.get('username'))
                if accountExistObj:
                    Account.objects.filter(username=request.session['username']).update(logged = True)
                    #notification time and date
                    messageObj = " logged-in on: " + str(datetime.datetime.now())
                    notifyObj = Notifications(user_id = user_obj[0].id , friend_id = user_obj[0].username, message = messageObj)
                    notifyObj.save()
                else:
                    createAccount = Account(id=request.session['user_id'],username=request.session['username'], password=hashed_password, logged = True)
                    createAccount.save()
            else:
                return HttpResponse("<script>alert('Account is locked. Please press logout when logging out. Click OK and wait for 1 minute then log in.');window.location = '/account-locked/" + request.POST.get('username') + "'; </script>")

        return HttpResponseRedirect('/home')
