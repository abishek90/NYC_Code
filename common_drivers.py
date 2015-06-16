# Test how many significant drivers pverlap between fare data set and trip data set

import csv
def mykey(local_list):
	return local_list[1]

def sort_dict_value(dict_data,rev_flag): # Set rev_flag to flase if want in ascending order
	list_d = []
	for ite in dict_data:
		list_d.append([ite,dict_data[ite]])
	dict_return = sorted(list_d,key=mykey,reverse=rev_flag)
	return dict_return

def test_uniqueness(col_name):
		col_dict = {}
		ini_flag =0
		fname = 'data'

		for i in range(12):
			with open('../../Data/trip_'+fname+'_'+str(i+1)+'.csv') as f_data:
				rowreader = csv.reader(f_data,delimiter=',')
				
				nfile_flag = 0
				for row in rowreader:
					if ini_flag == 0:
						if col_name in row:
							col_index = row.index(col_name)
						else:
							print str(i+1) + '  ' + row[3]
							sys.exit(0)
						
						ini_flag = 1
						continue
					else:
						if nfile_flag == 0:
							nfile_flag = 1
							continue
						if row[col_index] in col_dict:
							col_dict[row[col_index]]+=1
						else:
							col_dict[row[col_index]]=1



		# Print out the top value of the reverse sorted list according to the key value of the dict
		#sorted_dict_data = sort_dict_value(col_dict,True)
		# count = 1
		# print ' The Number of distinct Keys ' + str(len(sorted_dict)) + '\n'
		# with open('../../Data/significant_drivers.csv','w') as f_drive_write:
		# 	for ite in sorted_dict:
		# 		#print str(ite[0]) + ' ' + str(ite[1])
		# 		drive_write = csv.writer(f_drive_write,delimiter=',')
		# 		drive_write.writerow([str(ite[0]) , (ite[1])])
		# 		count+=1
		# 		# if count == 31:
		# 		# 	print len(sorted_dict)
		# 		# 	break
		# 		if ite[1] < 13000:
		# 			print count
		# 			break

		# Here we have the list of significant drivers in data.

		fname = 'fare'
		col_dict_fare={}
		for i in range(12):
			print i
			with open('../../Data/trip_'+fname+'_'+str(i+1)+'.csv') as f_data:
				rowreader = csv.reader(f_data,delimiter=',')
				
				nfile_flag = 0
				for row in rowreader:
					if ini_flag == 0:
						if col_name in row:
							col_index = row.index(col_name)
						else:
							print str(i+1) + '  ' + row[3]
							sys.exit(0)
						
						ini_flag = 1
						continue
					else:
						if nfile_flag == 0:
							nfile_flag = 1
							continue
						if row[col_index] in col_dict_fare:
							col_dict_fare[row[col_index]]+=1
						else:
							col_dict_fare[row[col_index]]=1


		#sorted_dict_fare = sort_dict_value(col_dict,True)

		# Now compare the number of common drivers having larger than 1000 entries in both.
		common_count = 0;
		threshold_number = 1000
		with open('../../Data/common_drivers.csv','w') as f_common:
			for ite in col_dict:
				drive_id = ite;
				print ite
				
				if drive_id in col_dict_fare:
					
					if col_dict_fare[drive_id] > threshold_number and col_dict[ite]> threshold_number:
						common_count +=1
						drive_write = csv.writer(f_common, delimiter=',')
						drive_write.writerow([str(ite)])
			print 'The Number of Common Elements are \n'
			print common_count




def main():
	# Get the column name in a automated way from the appropriate file
	reqd_index = 1;
	fname = 'data'

	with open('../../Data/trip_' + fname+'_1.csv') as f_name:
		rowreader = csv.reader(f_name,delimiter=',')
		lco = 0
		for row in rowreader:
			col_name = row[reqd_index]
			print 'The Column under Consideration is ' + col_name + '\n'
			break
		test_uniqueness(col_name)

if __name__ == '__main__':
  main()
