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

from entities import UserInfo

def addUser(conn, user):

    assert isinstance(conn, MySQLConnection)
    assert isinstance(user, UserInfo)

#    cursor = conn.cursor()
#    sql = "insert into user () values (?, ?, ?, ?)"
#    cursor.prepare()
#    cursor()

# ------------------------------------------------------------------------------

##from __future__ import print_function
##from datetime import date, datetime, timedelta
##import mysql.connector
##
##cnx = mysql.connector.connect(user='scott', database='employees')
##cursor = cnx.cursor()
##
##tomorrow = datetime.now().date() + timedelta(days=1)
##
##add_employee = ("INSERT INTO employees "
##               "(first_name, last_name, hire_date, gender, birth_date) "
##               "VALUES (%s, %s, %s, %s, %s)")
##add_salary = ("INSERT INTO salaries "
##              "(emp_no, salary, from_date, to_date) "
##              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
##
##data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
##
### Insert new employee
##cursor.execute(add_employee, data_employee)
##emp_no = cursor.lastrowid
##
### Insert salary information
##data_salary = {
##  'emp_no': emp_no,
##  'salary': 50000,
##  'from_date': tomorrow,
##  'to_date': date(9999, 1, 1),
##}
##cursor.execute(add_salary, data_salary)
##
### Make sure data is committed to the database
##cnx.commit()
##
##cursor.close()
##cnx.close()

#-------------------------------------------------------------------------------

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
