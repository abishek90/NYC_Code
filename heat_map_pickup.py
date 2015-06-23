# Heat Map of Aggregated Pickup Locations

# Indices 10 and 11 are pickup lattitude and Longitude respectively

import sys
import csv
import matplotlib.pyplot as plt 
import numpy as np

x_vals_pickup =[]
y_vals_pickup = []

x_vals_drop = []
y_vals_drop = []

xmin = 0
xmax = -100
ymin = 100
ymax = 0




# Have a list of the significant Drivers

driver_list = {}

with open('../../Data/significant_drivers.csv') as f_drivers:
	rowreader = csv.reader(f_drivers,delimiter=',')

	for row in rowreader:
		driver_list[row[0]] = row[1]

# Go Through the data

for i in range(1):
	with open('../../Data/trip_data_'+str(i+1)+'.csv') as f_data:
		rowreader = csv.reader(f_data,delimiter=',')
		first_line = 0
		for row in rowreader:
			if first_line == 0:
				first_line =1
				continue
			else:
				curr_driver = row[1]
				if curr_driver in driver_list:
					try:
						t1 = float(row[10])
					except ValueError:
						print row 
						print row[11]
						print first_line
						print 'Number 10 is in Error'
						continue
					try:
						t2 = float(row[11])
					except ValueError:
						print row 
						print row[11]
						print first_line
						print 'Number 11 is in Error'
						continue
					
					try:
						t3 = float(row[12])
					except ValueError:
						print row
						print row[12]
						print first_line
						print 'Number 12 is in Error'
						continue
					
					try:
						t4 = float(row[13])
					except ValueError:
						print row
						print row[13]
						print first_line
						print 'Number 13 is in Error'
						continue



					if t1 < -75.8 or t1 > -74.2:
					
						continue
					if t3 < -75.8 or t3 > -74.2:
				
						continue
					if t2 < 40.5 or t2 > 41:
				
						continue
					if t4 < 40.5 or t4 > 41:
				
						continue



					if t1 < xmin:
						xmin = t1
					if t1 > xmax:
						xmax = t1

					if t3 < xmin:
						xmin = t3
					if t3 > xmax:
						xmax = t3

					if t2 < ymin:
						ymin = t2
					if t2 > ymax:
						ymax = t2

					if t4 < ymin:
						ymin = t4
					if t4 > ymax:
						ymax = t4

					x_vals_pickup.append(t1)
					x_vals_drop.append(t3)
					y_vals_pickup.append(t2)
					y_vals_drop.append(t4)

				first_line +=1

print "The X-min and X-max are " + str(xmin) + "  and " + str(xmax)
print "The Y-min and Y-max are " + str(ymin) + "  and " + str(ymax)

print len(x_vals_pickup)

heatmap_pickup,xedges,yedges = np.histogram2d(np.array(x_vals_pickup),np.array(y_vals_pickup),bins = (1000,1000))
extent = [xedges[0],xedges[-1],yedges[0],yedges[-1]]
heatmap_drop = np.histogram2d(np.array(x_vals_drop),np.array(y_vals_drop))
plt.clf()
plt.imshow(heatmap_pickup,extent=extent)
plt.show()

# plt.figure()
# plt.imshow(heatmap_drop)
# plt.show()
