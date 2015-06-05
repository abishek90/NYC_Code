# THis is a script file to see the different columns of data in the NYCData set
# Run this script to understand the meanings of the different columns Write this to a txt file that 
#can be kept open

import csv
with open('../../Data/trip_fare_1.csv') as f_trip:
	#with open('../../Data/trip_fare_1.csv') as f_fare
	ftxt = open('../../Data/col_headers_data.txt','w')

	rowreader = csv.reader(f_trip,delimiter=',');
	line_c = 1;
	for row in rowreader:
		print(' The row meanings in Fare Data \n ')
		print  '\n'.join(row)
		# Write this row into a text file
		word_c =0
		ftxt.write(' The row meanings in Fare Data \n \n ')
		for word in row:
			ftxt.write(word + ' - ' + str(word_c) + '\n')
			word_c +=1

		break
	
with open('../../Data/trip_data_1.csv') as f_data:
	ftxt
	rowreader = csv.reader(f_data,delimiter=',');
	for row in rowreader:
		print(' \n The column meanings in the Trip Data File \n ')
		ftxt.write('\n \n  The row meanings in Fare Data \n \n')

		print '\n'.join(row)
		print('\n')
		word_c = 0
		for word in row:
			ftxt.write(word + ' - ' + str(word_c) + '\n')
			word_c +=1

		break



