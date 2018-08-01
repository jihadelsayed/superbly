from sgcommapp.models import *
from django.views.generic import View
from django.http import HttpResponseRedirect


from random import randint

from .services import SuperblyServices


class LoginView(View):

    def get(self, request):
        pass

    def post(self, request):
        user_obj = Profile.objects.filter(username=request.POST.get('username'), password=request.POST.get('password'))
        if user_obj.count():
            request.session['user_id'] = user_obj[0].id
            request.session['username'] = user_obj[0].username
        return HttpResponseRedirect('/home')
