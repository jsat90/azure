import os
import sys
from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
import json
import requests
import urllib
from scipy.stats import *

url = 'https://data.gov.sg/api/action/datastore_search?resource_id=d3995be5-e79c-436b-8514-bee5de22799b'

json_data = requests.get(url).json()
#print json_data


#json_data = json.dumps(raw_data)
#print json_data
exit;
Year=[]
NetCapitalStock=[]

totalnumber=json_data["result"]["total"]

for i in range(totalnumber):
	a=json_data['result']['records'][i]['year']
	c=int(a)
	Year.append(c)
	b=json_data['result']['records'][i]['value']
	d=float(b)
	NetCapitalStock.append(d)

#print NetCapitalStock
Regression = polyfit(Year,NetCapitalStock,1)
r2 = polyfit(Year,NetCapitalStock,2)
r3 = polyfit(Year,NetCapitalStock,3)
print Regression

plot(Year,NetCapitalStock,'x')
plot(Year,polyval(Regression,Year),'r-')
plot(Year,polyval(r2,Year),'b--')
plot(Year,polyval(r3,Year),'m:')
print ("Linear regression R2 value: ")
slope,intercept,r_value,p_value,std_err = linregress(Year,NetCapitalStock)
print(pow(r_value,2))

print()


show()



