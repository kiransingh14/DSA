def uperLeftColumnTriangleInNumber(number):
    for i in range(1,number+1):
        for j in range(1, number-i+2):
            print(j, end =" ")
        print("\n")
number = int(input("Enter number:"))
uperLeftColumnTriangleInNumber(number)

'''
output:
    
1 2 3 4 5 6 7 

1 2 3 4 5 6 

1 2 3 4 5 

1 2 3 4 

1 2 3 

1 2 

1
'''