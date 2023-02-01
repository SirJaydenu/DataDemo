#CSV File Formating
categories = "Name, Color, Animal, Food"
data1 = "Jill, Black, Tiger, Hotdog"
#Using Split 
print(data1.split(", "))
#Importing From Another File
file = open("data.CSV", "r")# file name, r is read
print(file.readline())
