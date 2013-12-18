#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref

class Signal(object):

    def __init__(self):
        super(Signal, self).__init__()
        self.__weakrefedCallbacks = []

    def send(self, *args, **kwargs):
        for weakrefedCallback in self.__weakrefedCallbacks:
            cb = weakrefedCallback()        # unreference weak ref
            if cb is not None:
                assert callable(cb)
                cb(self, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.send(*args, **kwargs)

    def connect(self, cb):

        assert callable(cb)
        wref = weakref.ref(cb)
        if wref not in self.__weakrefedCallbacks:
            self.__weakrefedCallbacks.append(wref)    # add weak ref

    def disconnect(self, cb):
        wref = weakref.ref(cb)
        if wref in self.__weakrefedCallbacks:
            self.__weakrefedCallbacks.remove(wref)    # remove weak ref

# ------------------------------------------------------------------------------

def mycallback(sender, *args, **kwargs):
    print "mycallback func"
    print "sender: ", sender
    print "args: ", args
    print "kwargs: ", kwargs
    for key in kwargs:
        print key, "=>", kwargs[key]

class MyCallback(object):

    def __init__(self):
        super(MyCallback, self).__init__()

    def __call__(self, sender, *args, **kwargs):
        print "MyCallback class", sender, args, kwargs

def main():
    sig = Signal()
    sig.connect(mycallback)
    sig.connect(mycallback)
    mycb = MyCallback()
    sig.connect(mycb)
    print "-" * 80
    sig(1,2,3, hello="world", world= 3.14, u=u"unicode")
    mycb = None
    sig.disconnect(mycallback)
    print "-" * 80
    sig()
    print "-" * 80
    sig(1,2,3, hello="world", world= 3.14, u=u"unicode")
    #mycallback(1,2,3, hello="world", world= 3.14, u=u"unicode")

if __name__ == '__main__':
    main()
