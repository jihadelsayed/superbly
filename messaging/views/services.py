from sgcommapp.models import *

import urllib
import re

class SuperblyServices:
    def Test_User_Login(request):
        if 'user_id' not in request.session or 'username' not in request.session:
            return False
        else:
            return True

    def extract_urls(messages):
        urls = []
        # extract urls and add anchor tags
        urlpat = re.compile(r'https://[w{3}a-zA-Z0-9]*.[a-zA-Z0-9]+.[a-z{3}][,\b]*[[/a-zA-Z0-9-?=_+&.]*]*')

        urls = urlpat.findall(str(messages).replace(',', ' '))

        for url in urls:
            messages = messages.replace(url, "<a href='" + str(url) + "'>" + str(url) + "</a>")

        return messages
