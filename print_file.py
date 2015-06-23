# Print the first K lines of a file to test for anamolies
import sys
import csv
st1 = "";
st2 = ""
with open('../../Data/trip_data_1.csv') as f_trip:
	#with open('../../Data/trip_fare_1.csv') as f_fare
	

	rowreader = csv.reader(f_trip,delimiter=',');
	line_c = 1;
	for row in rowreader:
		
		if line_c == 1:
			if ' fare_amount' in row: 
				fare_index = row.index(' fare_amount')

			if ' tolls_amount' in row:
				toll_index = row.index(' tolls_amount')
			if ' hack_license' in row:
				license_index = row.index(' hack_license')
		if line_c == 2212381:

			print float(row[12]) 
			break
		#print row.index(' rate_code')

		st1 = row[3]
		line_c +=1
		# Write this row into a text file
		#if line_c == 12:
			#break

# with open('../../Data/trip_data_1.csv') as f_data2:
# 	rowreader = csv.reader(f_data2,delimiter=',')
# 	for row in rowreader:
# 		st2 = row[5];
# 		print row
# 		break
