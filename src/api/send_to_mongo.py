#!/usr/bin/env python

from __future__ import print_function
import binascii
import time
import sys
import datetime
import pymongo

from bson import json_util
from inovonics.echostream.radios import SerialRadioThread
from inovonics import *

logfile = open( "log.txt", "a+")

client = pymongo.MongoClient()
db = client.ihrs
collection = db.messages

##
# @brief prints hexadecimal serial message to console
# @param message is a decoded serial message
def printCallback( message):
    print ("Message: %s" % (  binascii.hexlify( message), ))

##
# @brief prints decoded serial message to a logfile in pretty JSON format
# @param message is a decoded serial message
def printMessage( message):
    global logfile
    try:
        print( message)
        print()
        m = message.getJSON()
        md = json_util.loads(m)
        print(m)
        collection.insert_one(md)
        print( "\n")
        logfile.write( str( message) + "\n")
        logfile.write( message.getPrettyJSON() + "\n\n")
    except Exception as ex:
        print ( ex)
        logfile.write( "BAD MESSAGE:\n")
        logfile.write( str( binascii.hexlify( message)))
        logfile.write( "\n\n")

def main():
    port = 'COM3'
    if len(sys.argv) > 1:
        port = sys.argv.pop()
    receiver = SerialRadioThread( port, printMessage)
    try:
        receiver.start()
        global logfile
        logfile.write( "--- " + str( datetime.datetime.now()) + " ---\n\n")
        while True:
            time.sleep( 5)
            print ( receiver.getStats())
    except KeyboardInterrupt:
        pass
    finally:
        receiver.stop()

if __name__ == '__main__':
    main()
