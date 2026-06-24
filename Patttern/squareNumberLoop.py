def squareNumberLoop(number):
    for i in range(0,2*number-1):
        for j in range(0,2* number-1): 
            top=i
            left=j
            right=(2*number-2)-j
            down=(2*number-2)-i
            print(number-min(min(top,down),min(right,left)), end=" ")
        print("")
   
number = int(input("Enter number:"))
squareNumberLoop(number)


'''
output:
Enter number:5
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 

'''
