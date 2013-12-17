#!/usr/bin/env python
# -*- coding: utf-8 -*-

from entities import UserInfo

import mysql.connector

config = {
  'user': 'root',
  'password': '123456',
  'host': '127.0.0.1',
  'database': 'demo',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]
cursor.close ()
cnx.close()

class Task(object):

    def init(self): pass
    def execute(self): pass
    def done(self): pass



class Signal(object):

    def __init__(self):

        super(Signal, self).__init__()
        self.callbacks = []

    def addCallback(self, cb):

        assert callable(cb)
        self.callbacks.append(cb)

    def removeCallback(self, cb):

        self.callbacks.remove(cb)

    def clearCallbacks(self):

        self.callbacks = []

    def notifyCallbacks(self, **kwargs):

        for cb in self.callbacks:
            cb(**kwargs)


class ResuablePool(object):

    def __init__(self, cls):    # TODO: max pool size

        super(ResuablePool, self).__init__()

        import inspect
        assert inspect.isclass(cls)

        self.cls = cls
        self.instances = []

    def get(self):

        if not self.instances:
            instance = self.cls()
            self.instances.append(instance)

        assert self.instances
        return self.instances.pop()

    def put(self, instance):

        assert isinstance(instance, self.cls)
        self.instances.append(instance)

    def clear(self):

        for instance in self.instances:
            instance.reusable = False
            instance.done()                 # TODO:

        self.instances = []

class ReusableTask(Task):

    def __init__(self, pool = None):

        super(ReusableTask, self).__init__()
        self.pool = pool
        self.reusable = self.pool is not None

    def done(self):

        if self.reusable:

            assert self.pool is not None
            self.pool.put(self)



class DbTask(Task):

    def __init__(self, sql, callback, **config):

        assert callable(callback)

        super(DbTask, self).__init__()

        self.connection = None
        self.sql = sql
        self.config = config

    def init(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(**self.config)

    def execute(self):
        cur = self.connection.cursor()
        cur.execute(self.sql)
        cur.close()

    def done(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None





def addUserIfNotExists(conn, user):

    assert isinstance(user, UserInfo)




def main():
    pass

if __name__ == '__main__':
    main()
