print ("""Welcome to IFSC Project 1 - Length of Time\n
This coding program will tell you how many years, days, hours, minutes, and seconds
are in a certain number of seconds, prompted to be entered by you.\n""")

a = int(input("Enter the Length of Time in Seconds: "))

seconds = int()
minutes = int()
hours = int()
days = int()
years = int()

years = a // 31536000
a = a % 31536000

days = a // 86400
a = a % 86400 

hours = a // 3600
a = a % 3600

minutes = a // 60
a = a % 60

seconds = a

print("Years: ", years)
print("Days: ", days)
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)
