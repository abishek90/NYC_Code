# This file is to compute the global temporal binnings of income, distance and hours driven by all drivers. The bins are days of the week, months of the year and hours of the day

# The gola is to generate three tables of sizez 7 times 3, 12 times 3 and 24 times 3. 

# These are data values averaged over drivers (having larger than 6000 records).

# The Row Headers : hours_pdf, hours_cond_avg, hours_uncond_avg, hours_count,
#                   distance_pdf, distance_cond_avg, distance_uncond_avg, distance_count,
#                   income_pdf, income_cond_avg, income_uncond_avg, income_count.


def getDay(month,date):
# Returns either 'Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday,'Friday','Saturday'
	return day 


def main():

	
	drive_dict = {}
	weekly_dict = {}
	monthly_dict = {}
	hourly_dict_weekday = {}
	hourly_dict_friday = {}
	hourly_dict_saturday = {}
	hourly_dict_sunday = {}
	with open('../../Data/significant_drivers.csv') as f_drivers:
		drive_read = csv.reader(f_drivers,delimiter=',')
		for row in drive_read:
			drive_read[row[0]] = row[1]
	# Write the Hours and Distance Logs
	for i in range(12):
		with open('../../Data/trip_data_'+str(i+1)+'.csv') as f_data:
			rowreader = csv.reader(f_data,delimiter=',')
			for row in rowreader:
				driver_id = row[1]
				if driver_id in drive_dict:
					# Update the Tables
					pickup_datetime = row[5]
					split1_datetime = pickup_datetime.split('-')
					month_pickup = int(split1_datetime[1])
					split2_datetime = split1_datetime[2].split(' ')
					split3_datetime = split2_datetime[1].split(':')
					hour_pickup = int(split3_datetime[0])
                    day_pickup = getDay(month_pickup,int(split2_datetime[0])) # This needs to be implemented yet
                    trip_distance = row[9]
                    trip_duration = row[8]

                    if day_pickup in weekly_dict:
                    	# Update that row
                    	local_week_row = weekly_dict[day_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	weekly_dict[day_pickup] = local_week_row
                    else:
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	weekly_dict[day_pickup] = local_week_row


                    if hour_pickup in hourly_dict_weekday:
                    	# Update the Existing Record
                    	local_week_row  = hourly_dict_weekday[hour_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	hourly_dict_weekday[hour_pickup] = local_week_row

                    else:
                    	# Create a new record
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	hourly_dict_weekday[hour_pickup] = local_week_row


                    if hour_pickup in hourly_dict_friday:
                    	# Update the record
                    	local_week_row = hourly_dict_friday[hour_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	hourly_dict_friday[hour_pickup] = local_week_row

                    else:
                    	# Create a new record
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	hourly_dict_friday[hour_pickup] = local_week_row

                    if hour_pickup in hourly_dict_saturday:
                    	# Update Record
                    	local_week_row = hourly_dict_saturday[hour_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	hourly_dict_saturday[hour_pickup] = local_week_row


                    else:
                    	# Create a record
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	hourly_dict_saturday[hour_pickup] = local_week_row

                    if hour_pickup in hourly_dict_sunday:
                    	local_week_row = hourly_dict_sunday[hour_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	hourly_dict_sunday[hour_pickup] = local_week_row
                    else:
                    	 # Create a record
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	hourly_dict_sunday[hour_pickup] = local_week_row

                    if month_pickup in monthly_dict:
                    	local_week_row = monthly_dict[month_pickup]
                    	local_week_row[0] += trip_duration
                    	local_week_row[1] += 1
                    	local_week_row[2] += trip_distance
                    	local_week_row[3] += 1
                    	monthly_dit[month_pickup] = local_week_row
                    else:
                    	local_week_row = [trip_duration,1,trip_duration,1,0,0]
                    	monthly_dict[month_pickup] = local_week_row


				else:
					continue






	# Process the income logs and populate the local dict

	for i in range(12):
		with open('../../Data/trip_fare_'+str(i+1)+'.csv') as f_fare:
			rowreader = csv.reader(f_fare,delimiter=',')
			for row in rowreader:
				driver_id = row[1]
				if driver_id in drive_dict:
					# Update the Tables

					pickup_datetime = row[5]
					split1_datetime = pickup_datetime.split('-')
					month_pickup = int(split1_datetime[1])
					split2_datetime = split1_datetime[2].split(' ')
					split3_datetime = split2_datetime[1].split(':')
					hour_pickup = int(split3_datetime[0])
                    day_pickup = getDay(month_pickup,int(split2_datetime[0])) # This needs to be implemented yet
                    trip_distance = row[9]
                    trip_duration = row[8]

                    if day_pickup in weekly_dict:
                    	# Update the record
                    	local_row = weekly_dict[day_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	weekly_dict[day_pickup] = local_row
                    else:
                    	# Create the record
                    	local_row = [0, 0, 0, 0, row[10], 1]
                    	weekly_dict[day_pickup] = local_row

                    if hour_pickup in hourly_dict_weekday:
                    	# Update Record
                    	local_row = hourly_dict_weekday[hour_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	hourly_dict_weekday[hour_pickup] = local_row
                    else:
                    	# Create Record
                    	local_row = [0, 0, 0, 0, row[10], 1]
                    	hourly_dict_weekday[hour_pickup] = local_row


                    if hour_pickup in hourly_dict_friday:
                    	# Update Record
                    	local_row = hourly_dict_friday[hour_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	hourly_dict_friday[hour_pickup] = local_row
                    else:
                    	# Create Record
                    	local_row = [0, 0, 0, 0, row[10], 1]
                    	hourly_dict_friday[hour_pickup] = local_row



                    if hour_pickup in hourly_dict_saturday:
                    	# Update Record
                    	local_row = hourly_dict_saturday[hour_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	hourly_dict_saturday[hour_pickup] = local_row
                    else:
                    	# Create Record
                    	local_row = [0, 0, 0, 0, row[10], 1]
                    	hourly_dict_saturday[hour_pickup] = local_row

                    if hour_pickup in hourly_dict_sunday:
                    	# Update Record
                    	local_row = hourly_dict_weekday[hour_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	hourly_dict_sunday[hour_pickup] = local_row
                    else:
                    	# Create Record
                    	local_row = [0, 0, 0, 0, row[10], 1]
                    	hourly_dict_sunday[hour_pickup] = local_row

                    if month_pickup in monthly_dict:
                    	local_row = monthly_dict[month_pickup]
                    	local_row[4] += row[10]
                    	local_row[5] += 1
                    	monthly_dict[month_pickup] = local_row
                    else:
                    	local_row = [0, 0, 0, 0, row[10],1]
                    	monthly_dit[month_pickup] = local_row


				else:
					continue



	# Write the Dicts into 3 csv files that can be read by R