"""
Enter the temperature in celsius, and convert the 
temperature to fahrenheit. Finally, display different fever
 levels of the user.

fahrenheit = 9/5*celsius + 32
Conditions:
Temperature	Remarks
below 96F	Low Temperature
96F to 98F	Normal Temperature
99F to 101F	Normal Fever
102F to 104F	High Fever
above 104F	Critical

"""


c_temp = int (input("Enter the celsiu temprature: "))

f_temp = 9/5*c_temp + 32
print(f_temp)


if f_temp < 96:
    print('Low Temperature') 
if (f_temp <=98 and f_temp > 96):
    print('Normal Temperature')
if (f_temp >98 and f_temp <= 101):
    print('High Temperature')
if f_temp >101:
    print('Critical Tempeture')



       
    









