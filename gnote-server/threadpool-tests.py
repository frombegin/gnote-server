#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threadpool
import time

import mysql.connector

config = {
  'user': 'root',
  'password': '123456',
  'host': '127.0.0.1',
  'database': 'demo',
  'raise_on_warnings': True,
}

connections = []

def getConnection():

    if not connections:
        cnx = mysql.connector.connect(**config)
        connections.append(cnx)
    return connections.pop()

def releaseConnection(conn):

    if len(connections)<10:
        connections.append(conn)
        #print len(connections)
    else:
        print "conn full"
        conn.close()

def testMysql(*args, **kwargs):

    #cnx = mysql.connector.connect(**config)
    cnx = getConnection()
    cursor = cnx.cursor()
    cursor.execute ("SELECT VERSION()")
    row = cursor.fetchone ()
    #print "server version:", row[0]
    cursor.close ()
    #cnx.close()
    releaseConnection(cnx)

def workRun(*args, **kwargs):
    #print "workRun entering..."
    #time.sleep(2)
    testMysql()
    #print args, kwargs
    #print "workRun exiting..."
    return 3.14, "long long ago"

def workDone(req, *args):
    #print "work Done...", req, args
    pass

def method1():

    pool = threadpool.ThreadPool(10)
    for i in xrange(0,1000):
        wr = threadpool.WorkRequest(testMysql, args=[{"one":1, "two":3.14}], callback=workDone)
        pool.putRequest(wr)
    pool.wait()

def method2():
    for i in xrange(0,1000):
        testMysql()

from datetime import datetime

def main():
    print datetime.now()
    method2()
    print datetime.now()


if __name__ == '__main__':
    main()
