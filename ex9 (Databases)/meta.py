import sqlite3
import json
import os
import sys
import pandas as pd

db=sqlite3.connect("yada.db")
iterator=db.cursor()

def listAllTables():
    print "The tables are:"
    iterator.execute("select name from sqlite_master where type='table'")
    recordlib = iterator.fetchall()
    for x in range(0,len(recordlib)):
        print ("Table {}: {}".format(x+1,recordlib[x][0]))

def displayAllDataForTables():
    print "The meta data for all the tables are"
    iterator.execute("select name from sqlite_master where type='table'")
    alltab=iterator.fetchall()
    dummycursor=db.cursor()
    for record in alltab:
        print "The meta data of table of the name: {} are".format(record[0])
        dummycursor.execute("PRAGMA table_info("+record[0]+");")
        for x in dummycursor.fetchall():
            print "Column Number:{}\t Column Name:{}\t Datatype:{}\t Nullable:{}".format(x[0],x[1],x[2],(False if x[0]==1 else True))

listAllTables()
displayAllDataForTables()