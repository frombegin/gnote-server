#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string
from functools import partial

# ------------------------------------------------------------------------------


def randomString(length=10, allowedChars=string.ascii_letters):
    """randomString(int, [str]) -> str

    Returns a random string, char is from allowedChars.
    """

    return ''.join(random.choice(allowedChars) for i in range(length))


# ------------------------------------------------------------------------------


ALLOWED_PASSWORD_CHARS = string.digits + string.letters

randomPassword = partial(randomString, allowedChars=ALLOWED_PASSWORD_CHARS)
randomPassword.__doc__ = """randomPassword(int) -> str

create random password of given length (default is 10).
"""


# ------------------------------------------------------------------------------


import hmac

SECRET_KEY = "P`5[}=>+Ii"

def cryptPassword(password):
    """cryptPassword(str) -> str

    crypt password using HMAC for saving and authenticating
    """

    return hmac.new(SECRET_KEY, password).hexdigest()


# ------------------------------------------------------------------------------


def main():
    print randomString(10)
    print randomPassword()
    print cryptPassword("lmUIFLbhsc")
    print randomString.__doc__
    print randomPassword.__doc__
    print cryptPassword.__doc__

if __name__ == '__main__':
    main()
