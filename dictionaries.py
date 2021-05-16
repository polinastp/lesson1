weather = { "city" : "Moscow", "temperature" : "20"}
print(weather["city"])

a = int(weather["temperature"])
b = a - 5
a = b 
weather["temperature"] = a
print(a)
print(weather)

weather["country"] = "Russia"
weather["date"] = "21.05.2019"
print(len(weather))
print(weather)