def hollowSquare(number):
    for i in range(0,number):
        for j in range(0, number): 
            if(i==0 or j == 0 or i==number-1 or j == number-1):
                print("*", end =" ")
            else:
                print(" ", end =" ")
        print("")
   
number = int(input("Enter number:"))
hollowSquare(number)


'''
output:
Enter number:5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
