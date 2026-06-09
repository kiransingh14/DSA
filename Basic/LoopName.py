def printName(number, name):
    # for loop
    # for _ in range(number):
    #     print(name)
    
    
    #while loop
    i=0
    while(i<number):
        i+=1
        print(name)
name =input("Enter name:")
number =int(input("Enter how many number of time name should be printed:")) 
printName(number,name)