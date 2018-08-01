from django.http import HttpResponseRedirect
from django.views.generic import View
from messaging.views.messagesObj import *

import reportlab
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.pdfgen import canvas
from textwrap import wrap
from reportlab.lib.styles import getSampleStyleSheet

from django.http import HttpResponse
from sgcommapp.models import *


from .services import SuperblyServices


class DownloadMessages(View):
    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
                    
        # Create the HttpResponse object with the appropriate PDF headers.
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="superbly_saved_messages.pdf"'

        # userObj = User.objects.filter(id=request.session['user_id']) #7
        # friendObj = Friends.objects.filter(friend_id = userObj[0].username) #jun

        friendMsgObj = messagesObj(request)
        friendObj = friendMsgObj.getFriendObj()

        #userId = ""
        messageList = []
        for friend in friendObj:
            messageIdObj = SavedMessages.objects.filter(friend_id=friend.id)
            #print(friend.user_id) #12 16 19 20 1
            if messageIdObj.count() > 0:
                for messages in messageIdObj:
                    friendSender = Profile.objects.filter(id=friend.user_id)
                    messageList.append(messages.message + " | " + friendSender[0].username + " \n ")

        messageList.reverse()

        messageStr = "<b>Superbly Great</b> <br/><br/>"

        for message in messageList:
            messageStr = messageStr + message + "<br/><br/>"

        styles = getSampleStyleSheet()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="superbly_saved_messages.pdf"'
        #c = canvas.Canvas(response)
        #t = c.beginText()
        #t.setFont('Helvetica-Bold', 10)
        #t.setCharSpace(3)
        #t.setTextOrigin(50, 700)
        style = styles["Normal"]
        #wrapped_text = "\n".join(wrap(messageStr, 65))  # 80 is line width
        text = []
        # extract urls and add anchor tags
        messages = SuperblyServices.extract_urls(messageStr)

        wrapped_text = Paragraph("<para textColor='black'>" + messages + "</para>", style)
        text.append(wrapped_text)
        doc = SimpleDocTemplate(response)
        doc.build(text)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.

        # drawString location calculation.
        #x = 0
        #y = 8.5 * 72
        #t.textLines(wrapped_text, trim=1)
        #c.drawText(t)
        # Close the PDF object cleanly, and we're done.
        #c.showPage()
        #c.save()
        return response

    def post(self, request):
        pass
