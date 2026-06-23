def upperLeftTriangleStars(number):
    for i in range(0,number):
        for _ in range(0,number-i):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
upperLeftTriangleStars(number)


'''
output:
* * * * * * 

* * * * * 

* * * * 

* * * 

* * 

* 

'''
