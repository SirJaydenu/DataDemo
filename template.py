
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
	monthAvgList = []
	avg = []
	y=0
	for a in data_list:
		#a is the row x should be the next row
		print(index(a))
		date = a[0][:7]
		currdate = x[0][:5]
		v1 = a[5]
		c1 = a[6]
		v2 = x[5]
		c2 = x[6]
		print(" v1: "+v1+" c1: " + c1 +" v2: "+v2+" c2: "+c2)
		if currdate == date:
			tuple.append(((v1 * c1 + v2 + c2) / (v1 + v2)))
		elif currdate == date and currdate != year:
			tuple.append(((v1*c1) / v1))
		else:
			print("woo")
		monthAvgList.append(tuple())
		y+=2
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
