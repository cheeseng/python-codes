#!/usr/bin/python

import imaplib,datetime
import argparse
import dateutil.parser as dparse
import datetime as dates
import sys

#Fill in for logging in
USERNAME = ''
PASSWORD = ''


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--since", help = "Starting date", metavar = "[DATE | yesterday | today]")
parser.add_argument("-a", "--all", help = "Include all mails, seen too", action = "store_true")
parser.add_argument("-m", "--mailbox", help = "Get mails from this mailbox", metavar = "MailBox")
parser.add_argument("-l", "--list", help = "List all mailboxes", action = "store_true")
parser.add_argument("-c", "--count", help = "Only count number of mails", action = "store_true")
args = parser.parse_args()
# Date
if args.since:
    if args.since.lower() == 'yesterday':
        datef = dates.date.today() - dates.timedelta(days = 1)
    elif args.since.lower() == 'today':
        datef = dates.date.today()
    else:
        datef = dparse.parse(args.since, dayfirst = True, fuzzy = True)
else:
    datef = dates.date.today()
datef = datef.strftime('%d-%b-%Y')
# Mail type
if args.all:
    seen_mail = ")"
else:
    seen_mail = " UnSeen)"

try:
    obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
    obj.login(USERNAME, PASSWORD)
    print 'Logged in..'
    if args.list:
        lst = obj.list()
        for m in lst[1]:
            m = m.strip("'") 
            m = m.split(')')[1].split('"')[-2]
            print m
    else:
        #Mail folder
        if args.mailbox:
            obj.select(args.mailbox)
        else:
            obj.select()

        src = '(SINCE ' + datef + seen_mail
        print src
        l = obj.uid('search', None, src)
        lst = l[1][0].split()
        if args.count:
            print 'Number of mails received:', len(lst)
        else:
            for uid in lst:
                res = obj.uid('FETCH', uid, '(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])')
                print res[1][0][1]
    obj.logout()
except:
    print 'Network error..'
