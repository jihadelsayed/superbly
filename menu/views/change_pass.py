from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from sgcommapp.models import *
from django.template import RequestContext
from django.views.generic import View
from django.shortcuts import render

from .services import SuperblyServices

import random


class ChangePassword(View):
    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        template_name = 'change_pass.html'

        userName = request.session['username']
        new_passObj = SuperblyServices.pass_generate(request)
        user_pass_obj = Profile.objects.filter(id=request.session['user_id'])
        old_passObj = user_pass_obj[0].password
        variables = {'username': userName, 'old_pass': old_passObj, 'new_pass': new_passObj}
        return render(request, template_name, variables)


    def post(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
            
        userName = request.session['username']
        currentPassword = request.POST.get('currentpass')
        newPassword = request.POST.get('newpass')
        newPassword2 = request.POST.get('newpass2')
        if currentPassword and newPassword and newPassword2:
            userObj = Profile.objects.filter(username=userName)
            if userObj[0].password == currentPassword:
                if newPassword == newPassword2:
                    userObj = Profile.objects.get(username=userName)
                    # print(newPassword)
                    userObj.password = newPassword
                    userObj.save()
                    return HttpResponse(
                        "<script>alert('Password Updated. Keep safe your new password.');window.location = '/home'</script>")
                else:
                    return HttpResponse(
                        "<script>alert('Passwords do not match.');window.location = '/change-pass'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Wrong Current Password.');window.location = '/change-pass'</script>")
        else:
            return HttpResponse(
                "<script>alert('One of the password text boxes is empty.');window.location = '/change-pass'</script>")
