# This is to generate the CDF of the number of records per driver

import sys
import csv
import matplotlib.pyplot as plt



def test_validity(row):
		judgement = 'true'
		try:
			t1 = float(row[10])
		except ValueError:
				judgement = 'false'
				return judgement
		try:
			t2 = float(row[11])
		except ValueError:
				judgement = 'false'
				return judgement
			
		try:
			t3 = float(row[12])
		except ValueError:
			judgement = 'false'
			return judgement
		try:
			t4 = float(row[13])
		except ValueError:
			judgement = 'false'
			return judgement


		if t1 < -86 or t1 > -61:
			judgement = 'false'
		if t3 < -86 or t3 > -61:
			judgement = 'false'
		if t2 > 54 or t2 < 29:
			judgement = 'false'
		if t4 > 54 or t4 < 29:
			
			judgement = 'false'
		return judgement


list_cdf = [0]
dict_driver = {}

for i in range(12):
	with open('../../Data/trip_data_'+str(i+1)+'.csv') as f_data:
		rowreader = csv.reader(f_data,delimiter=',')
		first_row = 0;

		for row in rowreader:
			if first_row == 0:
				first_row = 1
				continue
			else:
				driver_id = row[1]
				if driver_id in dict_driver:

					# CHECK IF THE RECORD IS CLEAN
					if test_validity(row) == 'false':
						continue
					dict_driver[driver_id]+=1; 
					# Redistribution of Mass
					curr_val = dict_driver[driver_id]
					last_list_val = list_cdf[len(list_cdf)-1]
					if(len(list_cdf)-1) < curr_val:
						# Append the list
						list_cdf.append(last_list_val)
					else:
						list_cdf[curr_val] +=1





				else:
					dict_driver[driver_id] = 1 
					# Increase in Mass
					list_cdf[0] += 1
					if (len(list_cdf) > 1):
						list_cdf[1] +=1
					else:
						list_cdf.append(1)

				

print "number of records are :" + str(list_cdf[0])
plt.plot(list_cdf[1:])
plt.xlabel('number of records')
plt.show()

