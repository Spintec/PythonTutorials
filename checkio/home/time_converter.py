def time_converter(time):
    time_dictionary = {}

    for i in range(1, 13):
        time_dictionary[i] = i + 12
    x = int(time.split(":")[0])
    if int(time.split(":")[0]) == 12:
        return time + " p.m."
    elif int(time.split(":")[0]) in range(1, 12):
        return time.split("0")[1]+time.split(":")[1] + " a.m."

    elif int(time.split(":")[0]) in range(12, 24):
        twelve_h = (list(time_dictionary.keys())[list(time_dictionary.values()).index(x)])
        return str(twelve_h) + ":" + time.split(":")[1] + " p.m."
    else:
        return "12"+":"+time.split(":")[1]+" a.m."


print(time_converter('12:30'))
print(time_converter('09:00'))
print(time_converter('23:15'))
print(time_converter('18:50'))
print(time_converter('00:01'))