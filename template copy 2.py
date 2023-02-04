def getDataList(fileName):
	dataFile = open(fileName, "r")
	dataList = []
	for line in dataFile:
		return dataList
def getMonthlyAverage(dataList):
	m ='08'
	n='2008'
	monthlyAverageList=[]
	numerator=0.0
	denominator=0.0
	for i in dataList:
		#print i
		month=i[0].split('-')[1]
		year=i[0].split('-')[0]
		close=float(i[6])
		volume=float(i[5])
		if month!=m:
			average=numerator/denominator
			a_tuple=(month, year, average)
			monthlyAverageList.append(a_tuple)
			numerator+=close*volume
			denominator+=volume
			m=month
			n=year
			print monthlyAverageList
	return monthlyAverageList
def printInfo(monthlyAverageList):
	monthlyAverageList.sort()
	print 'The 6 best averages for google are:'
	print monthlyAverageList
	monthlyAverageList.reverse()
	print 'The 6 worst averages for google are:'
	print monthlyAverageList
	fileName='table.csv'
	dataList=getDataList(fileName)
	dataList.pop(0)
monthlyAverageList=getMonthlyAverage(dataList)
#print monthlyAverageList
printInfo(monthlyAverageList)