# THis is a script file to see the different columns of data in the NYCData set
# Can you compute the average amount paid to a taxi.

import csv
import sys
import numpy as np
num_records = [];
run_avg = [];
for i in range(12):
	with open('../../Data/trip_fare_' + str(i+1) + '.csv') as f_trip:
		#with open('../../Data/trip_fare_1.csv') as f_fare:

		rowreader = csv.reader(f_trip);
		index_flag = 1
		local_run_sum = 0;
		local_num_records = 0;
		# Find the column index of total amount.
		for row in rowreader:
			# Find the index first
			if index_flag == 1: 
				for name in row:
					total_amt_index = row.index(' tip_amount')
					total_fare_index = row.index(' fare_amount')
					total_toll_index = row.index(' tolls_amount')
				index_flag +=1;
			else:
				if float(row[total_fare_index]) + float(row[total_toll_index]) == 0:
					continue
				local_run_sum = local_run_sum + 100*(float(row[total_amt_index])/(float(row[total_fare_index]) + float(row[total_toll_index])));
				local_num_records +=1;
		run_avg.append(local_run_sum/local_num_records)
over_avg = np.mean(run_avg)
print ('The average tip percentage in the data set is :' + str(over_avg) + '  and the number of records is ' + str(num_records))


