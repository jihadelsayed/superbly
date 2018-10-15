from sgcommapp.models import *
from django.template.context_processors import csrf
from django.views.generic import View
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from random import randint

from .services import SuperblyServices
from .captcha import CaptchaObj
from .profile import ProfileObj

class SignupView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            captcha = CaptchaObj(request)
            result = captcha.validate()
            if result:
                obj = form.save()
                #replace string password to hash
                profile = ProfileObj(request)
                hashed_password = profile.replacePassword()
                profile.saveProfile()
                #create session cookies
                user_id, username = profile.createSession(obj)
                #logged account
                createAccount = Account(id=user_id,username=username, password=hashed_password, logged = True)
                createAccount.save()

                return HttpResponse("<script>alert('Sign-up Successful.');window.location = '/home'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Wrong Captcha Answer. Please refer to Help.');window.location = '/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Duplicate Username. Please pick a different Username.');window.location = '/'</script>")

        return HttpResponseRedirect('/')
