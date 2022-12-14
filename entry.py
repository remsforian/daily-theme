#import dependicies
from datetime import date
import csv
#bring in the csv file
with open("progress.csv", "a") as csvfile:
	#begin user inputs (must be integers)
	print("rate all of these words. Do not input a number greater than 10 or a decimal ")
	#rate "create" out of 10
	create = int(input('Rate "create" out of 10 '))
	#rate "discover" out of 10
	discover = int(input('Rate "discover" out of 10 '))
	#rate "work" out of 10
	work = int(input('Rate "work" out of 10 '))
	#rate "relationships" out of 10
	relationships = int(input('Rate "relationships" out of 10 '))
	#get today's date
	date = date.today()
	#write to csv
	writer = csv.writer(csvfile)
	writer.writerow([date, create, discover, work, relationships])
