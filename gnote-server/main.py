#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tornado.ioloop
import tornado.web

import binascii

class MainHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write("Hello, world")

    def _writeDict(self, d):
        for key, value in d.iteritems():
            self.write("%s -> %s\n" % (key, binascii.hexlify(str(value))))

    

    def post(self):
        self._writeDict(self.request.headers)
        self.write("\n")

        self.write("-"*40 + "\n")

        self._writeDict(self.request.files)
        self.write("\n")
        #self.write(self.request.body)

application = tornado.web.Application([
    (r"/", MainHandler),
], debug = True)

[
"user/register",
"user/login",
"user/logout",
"user/groups",

"lobby/findgroup",
"lobby/tags",
"lobby/finduser",
"lobby/timeline",

"group/create",
"group/join",
"group/invite",
"group/approval",
"group/post",
"group/timeline",

]


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()