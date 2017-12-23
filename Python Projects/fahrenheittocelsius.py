degree = input("Convert to Fahrenheit or celsius? For fahrenheit type 'f', for celsius type 'c'")
value = input("Insert temperature value: ")
value =int(value) 
if degree == "c":
    value = value-32
    value = value/1.8
    print(value) 
    
elif degree == "f":
    value = value*1.8 + 32
    print(value) 
    
else:
    print("Insert a valid value") 
