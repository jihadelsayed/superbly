from sgcommapp.models import *
from django.shortcuts import redirect

import random
import re
from hashlib import blake2b

class SuperblyServices:
    def Test_User_Login(request):
        if 'user_id' not in request.session or 'username' not in request.session:
            return False
        else:
            return True

    @staticmethod
    def pass_generate():
        # random password generator
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                  'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        lst = random.sample(values, 10)
        new_pass = ''.join(lst)

        return new_pass

    def hash_pass(password):
        m = blake2b(key=b'superbly', digest_size=16)
        m.update(password.encode('utf-8'))
        return m.hexdigest()

    def dedup(sndrMessageList, userIdOfSession, senderObj):  # Check for duplicates in messages list and remove them

        seen = set()
        sndCntr = 0
        sentCntr = False

        for item in sndrMessageList:
            if item not in seen:
                yield item + " | " + userIdOfSession + " to " + Friends.objects.get(
                    id=senderObj[sndCntr].friend_id).friend_id
                seen.add(item)
                sentCntr = False
            else:
                if not sentCntr:  # This lets the duplicated messages have only one "^^Sent to All" string ONCE.
                    yield "^^ Sent to All"
                    sentCntr = True
            sndCntr = sndCntr + 1

    def rep_sender(sndrList, userIdOfSession):
        # collect all record count that have ^^ Sent to all
        cntr = 0
        cntrList = []

        for snt in sndrList:
            if snt == "^^ Sent to All":
                cntrList.append(cntr)
            cntr = cntr + 1

        #  Replace friend id to send to all
        for x in range(len(sndrList)):
            if x in cntrList:
                str = sndrList[x - 1]
                startIndex = str.find("| " + userIdOfSession)
                endIndex = len(str)
                strmsg = str[startIndex:endIndex]
                # print(strmsg)
                sndrList[x - 1] = sndrList[x - 1].replace(strmsg, "| sent to all")

        # delete all items with "^^ Sent to all"
        for sndr in sndrList:
            if "^^ Sent to All" in sndr:
                sndrList.remove(sndr)

        return sndrList

    def extract_urls(messages):
        # find urls in messages and extract it. Separate links from messages.
        urls = []

        urlpat = re.compile(r'https://[w{3}a-zA-Z0-9]*.[a-zA-Z0-9]+.[a-z{3}][,\b]*[[/a-zA-Z0-9-?=_+&.]*]*')
        # find all links on messages and replace comma with whitespace.
        urls = urlpat.findall(str(messages).replace(',', ' '))

        link = list(range(len(urls)))

        return link, urls
