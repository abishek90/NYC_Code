# THis is a script file to see the different columns of data in the NYCData set
import csv
# with open('../../Data/trip_data_1.csv') as f_trip:
# 	#with open('../../Data/trip_fare_1.csv') as f_fare:

# 	rowreader = csv.reader(f_trip);
# 	count = 1
# 	for row in rowreader:
# 		print (row)
# 		count+=1;
# 		print('\n')
# 		if count == 3:
# 			break

with open('csvwrite_test.csv','w') as f_write:
	row_writer = csv.writer(f_write,delimiter =',');
	#row_writer.writerow([['Test']*3 , ['More Test'] , [str(33.4546)]])
	#row_writer.writerow([['Test']*2 , ['More Test'], [str(654446)]])
	row_writer.writerow(['Test', 'Hyper Test', 'Something More',3.14159])


with open('csvwrite_test.csv','r') as f_write_test:
	row_reader = csv.reader(f_write_test,delimiter=',')
	for row in row_reader:
		print(row.index('Test'))
		print('\n')