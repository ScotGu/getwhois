#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import whois
from time import sleep
from time import ctime
import time
sys.stderr = None

domain=sys.argv[1]

if domain.endswith(('tn','ci','xin','ke','dev','jp')) :
    print ("暂不支持此域名！")
else:
    dw=whois.whois(domain)
    print ("域名:", domain, end='|')
    print ("注册时间", end=':')
    if dw.creation_date :
        if len(str(dw.creation_date)) > 50 :
            print (dw.creation_date[0], end='|')
        elif len(str(dw.creation_date)) < 50 :
            print (dw.creation_date, end='|')
        else:
            print ("null-11", end='|')
    elif dw.registered :
        if len(str(dw.registered)) > 50 :
            print (dw.registered[0], end='|')
        elif len(str(dw.registered)) < 50 :
            print (dw.registered, end='|')
        else:
            print ("null-12", end='|')
    else:
        print ("无法查询", end='|')
        
    print ("到期时间", end=':')
    if dw.expiration_date :
        if len(str(dw.expiration_date)) > 50 :
            print (dw.expiration_date[0])
        elif len(str(dw.expiration_date)) < 50 :
            print (dw.expiration_date)
        else:
            print ("null-21")
    elif dw.expire :
        if len(str(dw.expire)) > 50 :
            print (dw.expire[0])
        elif len(str(dw.expire)) < 50 :
            print (dw.expire)
        else:
            print ("null-22")
    else:
        print ("无法查询")

