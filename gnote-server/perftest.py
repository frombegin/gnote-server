#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
#import tornado.gen
from tornado import gen
import tornado.httpclient

import time

from threading import Thread

class WorkerThread(Thread):

    def __init__(self, callback):
        super(WorkerThread, self).__init__()
        self.__callback = callback

    def run(self):
        time.sleep(3)
        iol = tornado.ioloop.IOLoop.instance()
        iol.add_callback(self.__callback, 2**100)

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.write("sleeping .... ")
        self.flush()
        yield gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 10.1)
        self.write("I'm awake, Hello, world")
        self.finish()

class ThreadHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://news.qq1.com", callback=self.on_response)

    def on_response(self, response):
        if response.error:
            self.write(response.body)
            self.flush()
            raise tornado.web.HTTPError(500)
        self.write("Fetched : %d bytes" % len(response.body) )
        self.finish()

class RealThreadHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        #self.write("start thread...<hr>\n")
        #self.flush()
        w = WorkerThread(self.on_response)
        w.start()

    def on_response(self, bignum):
        s = "thread done, bignum is \"%d\"" % bignum
        self.write({"result":s })
        self.finish()


class SubHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, sub")
        self.finish()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/sub/", SubHandler),
    (r"/thread/", ThreadHandler),
    (r"/realthread/", RealThreadHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    #try:
    tornado.ioloop.IOLoop.instance().start()
    #except KeyboardInterrupt:
    #    tornado.ioloop.IOLoop.instance().stop()