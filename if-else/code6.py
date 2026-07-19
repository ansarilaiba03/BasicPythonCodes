# take the input of temperatue in celsius
#below 0 degree C = freesing cold
# 0-10 degree C = very cold
# 10-20 degree C = cold
# 20-30 degree C = pleasant
# 30-40 degree C = hot
# above 40 degree C = very hot

temp = int(input("enter temp in degree celcius: "))

if temp < 0 :
    print("freezing cold")
elif temp > 0 and temp < 10:
    print("very cold")
elif temp > 10 and temp < 20:
    print("cold")
elif temp > 20 and temp < 30:
    print("pleasant")
elif temp > 30 and temp < 40:
    print("hot")
else:
    print("very hot")
