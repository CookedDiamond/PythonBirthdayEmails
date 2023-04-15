import csv
import datetime
from person import Person

def getBdayList():
	persons = []
	with open('birthdays.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			bday = datetime.datetime(int(row[4]), int(row[3]), int(row[2]))
			person = Person(row[0], row[1], bday)
			persons.append(person)
	return persons

# write csv year date 
