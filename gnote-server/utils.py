#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string
from functools import partial

# ------------------------------------------------------------------------------


def randomString(length=10, allowedChars=string.ascii_letters):
    """randomString(int, [str]) -> str

	����ָ�����ȵ�����ַ���, �ַ����� allowedChars �е��ַ����.
    """

    return ''.join(random.choice(allowedChars) for i in range(length))


# ------------------------------------------------------------------------------


ALLOWED_PASSWORD_CHARS = string.digits + string.letters

randomPassword = partial(randomString, allowedChars=ALLOWED_PASSWORD_CHARS)
randomPassword.__doc__ = """randomPassword(int) -> str

����ָ�����ȵ����봮 ( ���봮�е��ַ��� ALLOWED_PASSWORD_CHARS ��� )
"""


# ------------------------------------------------------------------------------


import hmac

SECRET_KEY = "P`5[}=>+Ii"

def cryptPassword(password):
    """cryptPassword(str) -> str

	ʹ�� HMAC ��������, ���ܺ���������ڱ��������ݿ��к͵�¼��֤
    """

    return hmac.new(SECRET_KEY, password).hexdigest()


# ------------------------------------------------------------------------------


def normalizeEmail(email):
    """ normalize_email(str) -> str

	��ָ�������ʼ���ַ�е���������ͳһΪȫ����Сд��ʽ ( code from django ;-) )
    """

    email = email or ''
    try:
        emailName, domainPart = email.strip().rsplit('@', 1)
    except ValueError:
            pass
    else:
        email = '@'.join([emailName, domainPart.lower()])
    return email


# ------------------------------------------------------------------------------


def main():
    print normalizeEmail("JOHN.smith@GOOGLE.com.Hk")
    print normalizeEmail(None)
    print normalizeEmail("JOHN.smith@GOOGLE.com.Hk")
    print randomString(10)
    print randomPassword()
    print cryptPassword("lmUIFLbhsc")

if __name__ == '__main__':
    main()
