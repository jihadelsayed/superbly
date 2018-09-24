from sgcommapp.models import *
from django.db.models import F
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
    def pass_generate(self):
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                  'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        lst = random.sample(values, 10)
        new_pass = ''.join(lst)

        return new_pass

    def hash_pass(password):
        m = blake2b(key=b'superbly', digest_size=16)
        m.update(password.encode('utf-8'))
        return m.hexdigest()
