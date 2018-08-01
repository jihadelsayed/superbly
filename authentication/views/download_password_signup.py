from django.http import HttpResponseRedirect
from django.views.generic import View

from django.http import HttpResponse
from sgcommapp.models import *

import reportlab
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

from .services import SuperblyServices

import datetime

class DownloadPasswordSignup(View):
    def get(self, request, new_pass):
        styles = getSampleStyleSheet()
        response = HttpResponse(content_type='application/pdf')

        # get date and time today
        dateToday = str(datetime.datetime.today())
        filename = "superbly-great-" + dateToday + "_" + "new_password.pdf"
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

        style = styles["Normal"]

        text = []

        messages = "<b>Superbly Great</b> <br/><br/>" + "<b>Date and Time:</b> " + dateToday + "<br/><br/>" + "<b>Password: </b>" + new_pass

        wrapped_text = Paragraph("<para textColor='black'>" + messages + "</para>", style)
        text.append(wrapped_text)
        doc = SimpleDocTemplate(response)
        doc.build(text)

        return response

    def post(self, request):
        pass