from csvread import getBdayList
import datetime
from emailsender import sendEmail

persons = getBdayList()
now = datetime.datetime.now()
for person in persons:
	if now.month == person.bday.month and now.day == person.bday.day:
		print("send email")
		sendEmail(person)
