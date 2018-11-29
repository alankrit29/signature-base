#!/usr/bin/python

import os, re
import sys
import smtplib
import email.utils
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText
msg = MIMEMultipart()

msg['Subject'] = sys.argv[1] + '\t' + 'Audit Report'
msg['To'] = ','.join([sys.argv[3]])
msg['From'] = sys.argv[2]
part = MIMEText('text', "plain")
part.set_payload('Please check the attached reports')
msg.attach(part)
session = smtplib.SMTP(sys.argv[5], 587)
session.ehlo()
session.starttls()
session.ehlo  
session.login(sys.argv[2], sys.argv[4])

fp = open('/var/log/yara_malicious_files.log', 'rb')
msgq = MIMEBase('text', 'text')
msgq.set_payload(fp.read())
fp.close()
encoders.encode_base64(msgq)
filename='yara_malicious_files.log'
msgq.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(msgq)
qwertyuiop = msg.as_string()

fp = open('/var/log/snyk_docker.log', 'rb')
msgq = MIMEBase('text', 'text')
msgq.set_payload(fp.read())
fp.close()
encoders.encode_base64(msgq)
filename='snyk_docker.log'
msgq.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(msgq)
qwertyuiop = msg.as_string()

fp = open('/var/log/lynis-vulnerable-packages.log', 'rb')
msgq = MIMEBase('text', 'text')
msgq.set_payload(fp.read())
fp.close()
encoders.encode_base64(msgq)
filename='lynis-vulnerable-packages.log'
msgq.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(msgq)
qwertyuiop = msg.as_string()

fp = open('/var/log/lynis-suggestions.log', 'rb')
msgq = MIMEBase('text', 'text')
msgq.set_payload(fp.read())
fp.close()
encoders.encode_base64(msgq)
filename='lynis-suggestions.log'
msgq.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(msgq)
qwertyuiop = msg.as_string()


session.sendmail(sys.argv[2], sys.argv[3], qwertyuiop)
session.quit()
