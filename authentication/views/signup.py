from sgcommapp.models import *
from django.template.context_processors import csrf
from django.views.generic import View
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from random import randint

from .services import SuperblyServices

class SignupView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            questionObj = Captcha.objects.get(question=request.POST.get('question'))
            answerStr = request.POST.get('answer')

            if questionObj.answer == answerStr.upper():
                obj = form.save()

                plain_username = request.POST.get('username')
                plain_password = request.POST.get('password')
                hashed_password = SuperblyServices.hash_pass(plain_password)

                profileObj = Profile.objects.get(username = plain_username)
                replace_pass = Profile(id=profileObj.id,username=profileObj.username, password=hashed_password)
                replace_pass.save()

                id = obj.id
                request.session['user_id'] = id
                request.session['username'] = form.cleaned_data['username']
                #logged account
                plain_password = request.POST.get('password')
                hashed_password = SuperblyServices.hash_pass(plain_password)
                createAccount = Account(id=request.session['user_id'],username=request.session['username'], password=hashed_password, logged = True)
                createAccount.save()

                return HttpResponse("<script>alert('Sign-up Successful.');window.location = '/home'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Wrong Captcha Answer. Please refer to Help.');window.location = '/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Duplicate Username. Please pick a different Username.');window.location = '/'</script>")

        return HttpResponseRedirect('/')
