def lowerTriangleStars(number):
    for i in range(0,number):
        for _ in range(0, i+1):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
lowerTriangleStars(number)


'''
output
* 

* * 

* * * 

* * * * 

* * * * * 

'''
