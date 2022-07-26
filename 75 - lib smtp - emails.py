import smtplib


sender = 'krwawymer@gmail.com'
recivers = ['mateusz.k.wojno@gmail.com', 'a.jablonowska97@gmail.com']

message = """From: From Nadawca <krwawymer@gmail.com> 
to: To Odbiorca <mateusz.k.wojno@gmail.com>, <a.jablonowska97@gmail.com> 
Subject: Wyslane z pythonga

Ago, wysylam Ci pythona 

()
=================================>
()
"""
try:
    mail = smtplib.SMTP('localhost')
    mail.sendmail(sender, recivers, message)
    print ('Email wyslany!')
except smtplib.SMTPException:
    print ("Error, nie udalo sie wyslac!")