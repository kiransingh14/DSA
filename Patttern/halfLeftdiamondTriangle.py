def halfLeftdiamondTriangle(number):
    for i in range(0,number):
        for _ in range(0, i+1):
            print("*", end =" ")
        print("\n")
    for i in range(1,number):
        for _ in range(0,number-i):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
halfLeftdiamondTriangle(number)


'''
output:
* 

* * 

* * * 

* * * * 

* * * * * 

* * * * * * 

* * * * * * * 

* * * * * * 

* * * * * 

* * * * 

* * * 

* * 

* 
'''
