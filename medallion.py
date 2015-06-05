# Understand if any column is unique identifier in the data
# One thing is to see is if the medallions are unique in a data file.
import csv
import sys

def mykey(local_list):
	return local_list[1]

def sort_dict_value(dict_data,rev_flag): # Set rev_flag to flase if want in ascending order
	list_d = []
	for ite in dict_data:
		list_d.append([dict_data.keys(),dict_data.values()])
	dict_return = sorted(list_d,key=mykey,reverse=rev_flag)
	return dict_return

def test_uniqueness(col_name):
	with open('../../Data/trip_data_1.csv') as f_data:
		rowreader = csv.reader(f_data,delimiter=',')
		medallion_d = {}
		ini_flag = 0;
		for row in rowreader:
			if ini_flag == 0:
				ini_flag = 1
				continue
			else:
				if row[0] in medallion_d:
					medallion_d[row[0]]+=1
				else:
					medallion_d[row[0]]=1
					print row[0]
					sys.exit(0)


		# Print out the top value of the reverse sorted list according to the key value of the dict
		sorted_dict = sort_dict_value(medallion_d,True)
		count = 1
		for ite in sorted_dict:
			print ite[1]
			count+=1
			if count == 2:
				break

def main():
	# Get the column name in a automated way from the appropriate file
	reqd_index = 0;
	fname = 'data'

	with open('../../Data/trip_' + fname+'_1.csv') as f_name:
		rowreader = csv.reader(f_name,delimiter=',')
		lco = 0
		for row in rowreader:
			col_name = row[reqd_index]
			break
		test_uniqueness(col_name)

if __name__ == '__main__':
  main()
