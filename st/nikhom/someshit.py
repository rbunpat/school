import datetime

start_time = input("Enter the start time: ")
end_time = input("Enter the end time: ")

end_time = datetime.datetime.strptime(end_time, '%H:%M')
start_time = datetime.datetime.strptime(start_time, '%H:%M')

time_difference = end_time - start_time

#if time_difference minutes is greater than 30, then add 1 to the hours and subtract 30 from the minutes
if time_difference.seconds // 60 > 30:
    hours = time_difference.seconds // 3600 + 1
#define a function called calprice
def calprice(hours):
#if hours is 2 or 3, multiply hours by 15
    if hours == 2 or hours == 3:
        price = hours * 15
#if hours is 4 or 5, multiply hours by 20
    elif hours == 4 or hours == 5:
        price = hours * 20
#if hours is 6 or 7, multiply hours by 25
    elif hours == 6 or hours == 7:
        price = hours * 25

#if hours is less than 1, print free
if time_difference.seconds // 3600 < 1:
    print("Free")
#else if hours is greater than 1, execute func1
elif time_difference.seconds // 3600 > 1:#
    calprice(hours)





#print out the result
#print(hours)

#print("The time difference is: ", time_difference)
