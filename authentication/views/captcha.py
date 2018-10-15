from sgcommapp.models import *

from random import randint

class CaptchaObj():
    def __init__(self, request):
        self.req = request

    def validate(self):
        questionObj = Captcha.objects.get(question=self.req.POST.get('question'))
        answerStr = self.req.POST.get('answer')

        if questionObj.answer == answerStr.upper():
            return True
        else:
            return False

    def createRandomCaptcha(self):
        # generate captcha with random question.
        randomId = randint(1, 20)
        captchaObj = Captcha.objects.filter(id=randomId)
        questionObj = str(captchaObj[0].question)

        return questionObj
