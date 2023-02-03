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
	month = data_list[0][0][5:7]
	res = []
	res2 = []
	x = 0
	for a in range(len(data_list)):
		if data_list[a][0][5:7] == month:
			a -= x
			v = data_list[a][6]
			c = data_list[a][5]
			res.append(float(v)*float(c))
			res2.append(float(v))
		else:
			x += 1
			avg.append(data_list[a-1][0][:7])
			avg.append(sum(res) / sum(res2))
			monthAvgList.append(tuple(avg))
			res = []
			res2 = []
			avg = []
			month = data_list[a][0][:7]
	avg.append(data_list[a-1][0][:7])
	avg.append(sum(res) / sum(res2))
	monthAvgList.append(tuple(avg))
	return monthAvgList
#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info(monthly_average_list):
	monthAvgList.sort()
	monthAvgList.reverse()
print_info(get_monthly_averages((get_data_list("table.csv"))))
# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the 
# return in monthly_average_list

# call print_info function with the monthly_average_list from above 
