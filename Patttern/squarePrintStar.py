def printStars(number):
    for _ in range(0,number):
        for _ in range(0, number):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
printStars(number)



'''
output:
* * * * * * * 

* * * * * * * 

* * * * * * * 

* * * * * * * 

* * * * * * * 

* * * * * * * 

* * * * * * * 
'''
