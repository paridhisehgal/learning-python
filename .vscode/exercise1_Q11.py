def temp_converter():
    temp = float(input ("enter temperature in celsius: "))
    value1 = (temp * 9/5)+ 32
    value2 = (temp + 273.15)
    
    print ("Temp in fahrenheit:",value1,"F")
    print ("Temp in kelvin:",value2,"K")


temp_converter()
