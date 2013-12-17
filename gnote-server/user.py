#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hmac

class UserDb(object):
    
    pass

SECRET_KEY = "!Q@W#E$R"

def cryptPassword(password):
    return hmac.new(SECRET_KEY, password).hexdigest()

class LoginException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

class UserNotExistsException(LoginException):
    pass

class PasswordWrongException(LoginException):
    pass

class DBException(Exception):
    pass

class Cache(object):
    
    pass

cache = Cache()

import re

def isValidEmail(email):
    '''Determine whether the given string is a valid email address.'''
    
    return re.match('[\w.%-]+@[\w.%-]+\.[a-zA-Z]{2,6}$', email)
  

def isValidName(name):
    pass

def isValidPassword(password):
    pass

class UserManager(object):
    
    def registerUser(self, name, email, password):
        
        assert isinstance(password, str) and isValidPassword(password)
        assert isinstance(email, str) and isValidEmail(email)
        assert isinstance(name, unicode) and isValidName(name)
        
        try:
            cryptedPassword  = cryptPassword(password)
            lastRowId = "insert into user (email, password) values (?, ?)"  #TODO: sql
            return User(lastRowId, name, email, cryptedPassword)
        except DBException as e:    # 
            raise UserAlreadyExistsException()
    
    def login(self, email, password):
        
        assert isinstance(password, str)
        assert isinstance(email, str)
        
        row = 'select * from user where email = ?'  #TODO: sql
        if not row:
            raise UserNotExistsException()
            
        if row['password'] != cryptPassword(password):
            raise PasswordWrongException()
        
        return User(row["id"], row["name"], row["email"])

    
    def getUserFromSession(self, sessionId):
        
        u = cache.get(sessionId, None)
        return u

    def logout(self, sessionId):
        
        cache.delete(sessionId)

class User(object):
    
    def __init__(self, uid, name, email):
        
        super(User, self).__init__()
        self.uid = uid
        self.name = name
        self.email = email 
 
def _main():
    pass

if __name__ == '__main__':
    _main()