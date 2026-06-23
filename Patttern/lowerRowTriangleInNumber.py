def lowerRowTriangleInNumber(number):
    for i in range(1,number+1):
        for _ in range(1, i+1):
            print(i, end =" ")
        print("\n")
number = int(input("Enter number:"))
lowerRowTriangleInNumber(number)

'''
output:
1 

2 2 

3 3 3 

4 4 4 4
'''