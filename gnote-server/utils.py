#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string
from functools import partial

# ------------------------------------------------------------------------------


def randomString(length=10, allowedChars=string.ascii_letters):
    """randomString(int, [str]) -> str

	返回指定长度的随机字符串, 字符串由 allowedChars 中的字符组成.
    """

    return ''.join(random.choice(allowedChars) for i in range(length))


# ------------------------------------------------------------------------------


ALLOWED_PASSWORD_CHARS = string.digits + string.letters

randomPassword = partial(randomString, allowedChars=ALLOWED_PASSWORD_CHARS)
randomPassword.__doc__ = """randomPassword(int) -> str

    返回指定长度的密码串 ( 密码串中的字符由 ALLOWED_PASSWORD_CHARS 组成 )
    """


# ------------------------------------------------------------------------------


import hmac

SECRET_KEY = "P`5[}=>+Ii"

def cryptPassword(password):
    """cryptPassword(str) -> str

	使用 HMAC 加密密码, 加密后的密码用于保存在数据库中和登录认证
    """

    return hmac.new(SECRET_KEY, password).hexdigest()


# ------------------------------------------------------------------------------


def normalizeEmail(email):
    """ normalize_email(str) -> str

	将指定电子邮件地址中的域名部分统一为全部是小写格式 ( code from django ;-) )
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
