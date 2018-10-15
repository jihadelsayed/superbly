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

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        template_name = "index.html"
        form = SignupForm()

        # generate captcha with random question.
        captcha = CaptchaObj(request)
        questionObj = captcha.createRandomCaptcha()
        # generate password generator
        new_passObj = SuperblyServices.pass_generate()

        return render(request, template_name, {'form': form, 'question': questionObj, 'new_pass': new_passObj})
