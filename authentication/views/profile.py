from sgcommapp.models import *

from .services import SuperblyServices

class ProfileObj():
    def __init__(self, request):
        self.req = request
        self.plain_username = self.req.POST.get('username')

    def replacePassword(self):
        #replace plain text to hash password
        self.plain_password = self.req.POST.get('password')
        self.hashed_password = SuperblyServices.hash_pass(self.plain_password)

        return self.hashed_password

    def createSession(self, obj):
        #create session cookies
        user_id = self.req.session['user_id'] = obj.id
        username = self.req.session['username'] = obj.username #form.cleaned_data['username']

        return user_id, username

    def saveProfile(self):
        profileObj = Profile.objects.get(username = self.plain_username)
        replace_pass = Profile(id=profileObj.id,username=profileObj.username, password=self.hashed_password)
        replace_pass.save()
