"""SuperblyGreat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.conf.urls import url
from authentication.views import signup
from authentication.views import main_page
from authentication.views import login
from authentication.views import logout
from authentication.views import home_page
from authentication.views import download_password_signup
from friends.views import add_friend
from friends.views import delete_friend
from friends.views import message_friend
from messaging.views import delete_messages
from messaging.views import delete_saved_messages
from messaging.views import download_messages
from messaging.views import save_messages
from menu.views import change_pass
from menu.views import download_password
from menu.views import delete_account


import os.path

urlpatterns = [
    path('', main_page.MainPageView.as_view()),
    path('signup', signup.SignupView.as_view()),
    path('login', login.LoginView.as_view()),
    path('home', home_page.HomePageView.as_view()),
    path('logout', logout.LogoutView.as_view(), name="logout"),
    path('add-friend', add_friend.AddFriend.as_view()),
    path('message-friend/<int:friend_id>', message_friend.MessageFriend.as_view()),
    path('delete-friend/<int:friend_id>', delete_friend.DeleteFriend.as_view()),
    path('delete-all-messages', delete_messages.DeleteMessages.as_view()),
    path('delete-all-saved-messages', delete_saved_messages.DeleteSavedMessages.as_view()),
    path('change-pass', change_pass.ChangePassword.as_view()),
    path('save-checked-messages', save_messages.SaveMessages.as_view()),
    path('download-saved-messages', download_messages.DownloadMessages.as_view()),
    path('download-password-signup/<str:new_pass>', download_password_signup.DownloadPasswordSignup.as_view()),
    path('download-password', download_password.DownloadPassword.as_view()),
    path('delete-account', delete_account.DeleteAccount.as_view()),
]
