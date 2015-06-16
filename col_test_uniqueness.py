# Understand if any column is unique identifier in the data
# One thing is to see is if the medallions are unique in a data file.
import csv
import sys

def mykey(local_list):
	return local_list[1]

def sort_dict_value(dict_data,rev_flag): # Set rev_flag to flase if want in ascending order
	list_d = []
	for ite in dict_data:
		list_d.append([ite,dict_data[ite]])
	dict_return = sorted(list_d,key=mykey,reverse=rev_flag)
	return dict_return

def test_uniqueness(col_name,fname):
		col_dict = {}
		ini_flag =0

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
		sorted_dict = sort_dict_value(col_dict,True)
		count = 1
		print ' The Number of distinct Keys ' + str(len(sorted_dict)) + '\n'
		for ite in sorted_dict:
			#print str(ite[0]) + ' ' + str(ite[1])
			print str(ite[0]) + ' ' + str(ite[1])
			count+=1
			# if count == 31:
			# 	print len(sorted_dict)
			# 	break
			if ite[1] < 12000:
				print count
				break

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
		test_uniqueness(col_name,fname)

if __name__ == '__main__':
  main()
