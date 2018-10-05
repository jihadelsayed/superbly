from sgcommapp.models import *


class notificationObj():
    def __init__(self, user_id, friend_id, message):
        self.user_id = user_id
        self.friend_id = friend_id
        self.message = message

    def saveNotification(self):
        notifyObj = Notifications(user_id = self.user_id , friend_id = self.friend_id, message = self.message)
        notifyObj.save()
