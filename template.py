#name: get_data_list
#param: FILE_NAME <str> - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists <list>
def get_data_list(FILE_NAME):
	FILE_NAME = open(FILE_NAME,  "r")
	list = []
	for line in FILE_NAME:
		list.append(line.strip().split(","))
	return list
#name: get_monthly_averages
#param: data_list <list> - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list <list>
def get_monthly_averages(data_list):
	del data_list[0]
	avg =[]
	monthAvgList = []
	numer = 0.0
	denom = 0.0
	month = data_list[0][0][:7]
	x = 1
	for a in data_list:
		print(a)
		close = float(a[6])
		volume = float(a[5])
		
		close2 = float(a+1[6])
		volume2 = float(a+1[5])
		numer = volume*close + volume2*close2
		denom = volume+volume2
		avg = numer/denom
		if data_list[x][0][:7] == month:
			
			tuple=(data_list[0][0][:7], avg)
			monthlyAverageList.append(tuple)
		numer += close * volume
		denom +=volume
		month = data_list[x][0][:7]
		print (monthAvgList)
		x+=1
	# 		a -= x
	# 		v = data_list[a][6]
	# 		c = data_list[a][5]
	# 		res = []
	# 		res2 = []
	# 		res.append(float(v)*float(c))
	# 		res2.append(float(v))
	# 	else:
	# 		x += 1
	# 		avg.append(data_list[a-1][0][:7])
	# 		avg.append(sum(res) / sum(res2))
	# 		monthAvgList.append(tuple(avg))
	# 		avg = []
	# 		month = data_list[a][0][:7]
	# avg.append(data_list[a-1][0][:7])
	# avg.append(sum(res) / sum(res2))
	# monthAvgList.append(tuple(avg))
	return monthAvgList
#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info(monthly_average_list):
	print("Top 6 Best Months for Google Stock: " , monthly_average_list.sort())
	print("Bottom 6 Worse Months for Google Stock: " , (monthly_average_list.reverse()))
print_info(get_monthly_averages((get_data_list("table.csv"))))
# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the 
# return in monthly_average_list

# call print_info function with the monthly_average_list from above 
