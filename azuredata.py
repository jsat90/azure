import requests
import sys
import json
from math import sin, cos, sqrt, atan2, radians

location1 = sys.argv[1]
location2 = sys.argv[2]

url1='https://maps.googleapis.com/maps/api/geocode/json?address=' + location1
url2='https://maps.googleapis.com/maps/api/geocode/json?address=' + location2


json1 = requests.get(url1).json()
#json2 = requests.get(url2).json()

latitude1 = json1['results'][0]['geometry']['location']['lat']
longitude1 = json1['results'][0]['geometry']['location']['lng']

json2 = requests.get(url2).json()

latitude2 = json2['results'][0]['geometry']['location']['lat']
longitude2 = json2['results'][0]['geometry']['location']['lng']

l1=float(latitude1)
l2=float(longitude1)
l3=float(latitude2)
l4=float(longitude2)

#approximation for the raduis of the earth

R=6373.0

lat1 = radians(l1)
lon1 = radians(l2)
lat2 = radians(l3)
lon2 = radians(l4)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat /2)**2 + cos(lat1) * sin(dlon / 2)**2
c = 2* atan2(sqrt(a), sqrt(1-a))


print "Distance in Kilometers is..."
distance = R * c

print distance




