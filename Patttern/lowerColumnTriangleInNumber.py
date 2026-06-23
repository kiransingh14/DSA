def lowerColumnTriangleInNumber(number):
    for i in range(1,number+1):
        for j in range(1, i+1):
            print(j, end =" ")
        print("\n")
number = int(input("Enter number:"))
lowerColumnTriangleInNumber(number)

'''
output:
1 

1 2 

1 2 3 

1 2 3 4 
'''