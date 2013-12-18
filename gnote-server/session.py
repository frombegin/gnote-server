#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


try:
    import cPickle as pickle
except ImportError:
    import pickle

def generateSessionId():

##        while True:
##            rand = os.urandom(16)
##            now = time.time()
##            secret_key = self._config.secret_key
##            session_id = sha1("%s%s%s%s" %(rand, now, utils.safestr(web.ctx.ip), secret_key))
##            session_id = session_id.hexdigest()
##            if session_id not in self.store:
##                break
##        return session_id

    # TODO:
    pass

def isValidSessionId(sessionId):

    return True

class Session(object):

    def __init__(self, sessionManager, sessionId = None):
        '''paramter sessionId is None or bad format, means a new created session'''

        super(Session, self).__init__()

        assert isinstance(sessionManager, AbstractSessionManager)
        self._sessionManager = sessionManager

        if not isValidSessionId(sessionId):
            self.sessionId = self._generateSessionId()
        else:
            assert isinstance(sessionId, str)
            self.sessionId = sessionId

        self.value = {}

    def __setitem__(self, key, value):

        self.value[key] = value

    def __getitem__(self, key):

        return self.value[key]

    def _generateSessionId(self):
        '''Generate a random id for session'''

        return generateSessionId()  #TODO:

    def save(self):

        s = pickle.dumps(self.value, 2)
        self._sessionManager.sessionSetValue(self.sessionId, s)

    def load(self):

        s = self._sessionManager.sessionGetValue(self.sessionId)
        if s is None:
            self.value = {}
        else:
            try:
                v = pickle.loads(s)
                if not isinstance(v, dict):
                    raise ValueError()
                self.value = v
            except:
                self.value = {}

    def kill(self):

        self._sessionManager.sessionDelete(self.sessionId)

class AbstractSessionManager(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def sessionExists(self, sessionId):
        '''return True if session exists'''

    @abstractmethod
    def sessionGetValue(self, sessionId):
        '''get value of session's key if exists, or None'''

    @abstractmethod
    def sessionSetValue(self, sessionId, value):
        '''set value of session's key'''

    @abstractmethod
    def sessionDelete(self, sessionId):
        '''delete session'''

    @abstractmethod
    def sessionCleanupExpired(self):
        '''cleanup expired sessions'''


def main():
    pass

if __name__ == '__main__':
    main()
