from sgcommapp.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View
from .services import SuperblyServices


class DeleteAccount(View):
    @staticmethod
    def purge_all(request):
        # Delete user logged in User model, Friends, Messages, Saved Messages
        userObj = Profile.objects.filter(username=request.session['username'])
        #print(request.session['username'])
        user = Profile.objects.filter(id=userObj[0].id)
        user.delete()

        # delete all friend id in Friends model
        friendObj = Friends.objects.filter(friend_id=request.session['username'])
        friendObj.delete()

        #TODO delete file uploads, files sent and file notes.
        #get id from Uploads using user_id, then match files_from_id and id (Uploads),
        #get note_id to match in filesnotes id

    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        userStr = request.session['username']
        data = {'username': request.session['username'],'user': userStr}
        return render(request, 'delete_account.html', data)

    def post(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        DeleteAccount.purge_all(request)
        #delete cookies
        request.session.clear()
        return HttpResponse("<script>alert('Your Account has been deleted. Logging out...');window.location = '/home'</script>")
