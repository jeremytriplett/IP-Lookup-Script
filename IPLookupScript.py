import requests
import datetime
import smtplib

gmail_user = 'redacted'
gmail_password = 'redacted'

sent_from = gmail_user
to = 'redacted'
subject = 'EOTU IP Report ' + str(datetime.datetime.now())
body= ''



usernamePA = 'redacted'
tokenPA = 'redacted'

class Access:
	def __init__(self, ip, place, rest):
	    self.ip = ip
	    self.place = place
	    self.rest = rest.decode()

response = requests.get('redacted'.format(username=usernamePA),
headers = {'Authorization': 'Token {token}'.format(token=tokenPA)})

data = response.content.splitlines()

accessList = []

for access in data:
    #Replace with regex
	ip = access.decode().partition('-')[0].strip()
	time = access.decode().partition('[')[2].partition(']')[0].partition('+')[0].strip()
	timeObj = datetime.datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')

	if timeObj > datetime.datetime.now() - datetime.timedelta(hours = 24):
		a = Access(ip, '', access)
		accessList.append(a)
hashmap = {}

for access in accessList:
	if(not access.ip in hashmap):
	    response = requests.get(redacted'.format(ip=access.ip))
	    data = response.json()
	    place = data['city'] + ' ' + data['region_name']
	    access.place = place
	    body += (access.place + '\n' + access.rest +  '\n\n')
	    hashmap[access.ip] = 1

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

if len(accessList)>0:
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print ('Email sent!')
    except:
        print ('Something went wrong...')
