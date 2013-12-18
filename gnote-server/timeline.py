#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta


class Activity(object):

    __metaclass__ = ABCMeta

class AbstractTimeline(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def pushActivity(self, activity):
        '''add a activity'''

    @abstractmethod
    def numActivities(self):
        '''number of Activities'''

    @abstractmethod
    def popNearestActivities(self, duration, maxResult = 100):
        '''get activities from duration ago to now, duration unit is seconds'''

        assert duration>0 and maxResult>0

        lastTime = datetime.now() - timedelta(seconds = duration)
        return self.getActivities(lastTime, maxResult)

    @abstractmethod
    def popActivities(self, fromTime, maxResult = 100):
        '''get activities from fromTime to now'''

class AbstractTimelineManager(object):

    __metaclass__ = ABCMeta

    def addTimeineActivity(self, name, activity):
        '''add a activity into timeline of the key'''

    @abstractmethod
    def getTimeline(self, name):
        '''get timeline if exists, or None'''

    @abstractmethod
    def addTimeline(self, name):
        '''add blank timeline'''

    @abstractmethod
    def removeTimeline(self, name):
        '''remove timeline'''

def main():
    pass

if __name__ == '__main__':
    main()
