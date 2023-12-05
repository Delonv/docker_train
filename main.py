import calendar

print ('Это мой обычный календрь')

year = int(input("Ввести год:"))
month = int(input("Ввести месяц:"))

print (calendar.month(year, month))