#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tornado.ioloop
import tornado.web

from threadpool import ThreadPool


class Application(tornado.web.Application):
    
    def __init__(self, handlers=None, default_host="", transforms=None,
                 wsgi=False, **settings):
        super(Application, self).__init__(handlers, default_host, transforms, wsgi, **settings)
        self.threadpool = ThreadPool(10)

class MainHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write("Hello, world")

#application = tornado.web.Application([
application = Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()