import datetime
start_time = input("Enter the start time: ")
end_time = input("Enter the end time: ")
end_time = datetime.datetime.strptime(end_time, '%H:%M')
start_time = datetime.datetime.strptime(start_time, '%H:%M')
time_difference = end_time - start_time
if time_difference.seconds // 60 > 30:
    hours = time_difference.seconds // 3600 + 1

def calprice(hours):
    global price
    if hours == 2 or hours == 3:
        price = hours * 15
    elif hours == 4 or hours == 5:
        price = hours * 15 + hours * 20
    elif hours == 6 or hours == 7:
        price = hours * 25
        
if time_difference.seconds // 3600 < 1:
    print("Free")
elif time_difference.seconds // 3600 > 1:#
    calprice(hours)
    print(price)
