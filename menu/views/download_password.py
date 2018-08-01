from sgcommapp.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View

import reportlab
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

import datetime

from .services import SuperblyServices


class DownloadPassword(View):
    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")

        styles = getSampleStyleSheet()
        response = HttpResponse(content_type='application/pdf')

        # get user password and username
        user_pass_obj = Profile.objects.filter(id=request.session['user_id'])
        old_passObj = user_pass_obj[0].password
        username = user_pass_obj[0].username

        # get date and time today
        dateToday = str(datetime.datetime.today())
        filename = "superbly-great-" + dateToday + "_" + username + ".pdf"
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

        style = styles["Normal"]

        text = []

        messages = "<b>Superbly Great</b> <br/><br/>" + "<b>Date and Time:</b> " + dateToday + "<br/><br/>" + "<b>Username: </b>" + username + "<br/><br/>" + "<b>Password: </b>" + old_passObj

        wrapped_text = Paragraph("<para textColor='black'>" + messages + "</para>", style)
        text.append(wrapped_text)
        doc = SimpleDocTemplate(response)
        doc.build(text)

        return response
