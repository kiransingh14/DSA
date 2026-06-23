def diamondTriangle(number):
    for i in range(1,number+1):
        for _ in range(1, number-i+1):
            print(" ", end =" ")
        for _ in range(1, 2*i):
            print("*", end =" ")
        for _ in range(1, number-i+1):
            print(" ", end =" ")
        print("\n")
    for i in range(1,number+1):
        for _ in range(1, i):
            print(" ", end =" ")
        for _ in range(1, (number*2-(2*i))+2):
            print("*", end =" ")
        for _ in range(1, i):
            print(" ", end =" ")
        print("\n")
number = int(input("Enter number:"))
diamondTriangle(number)

'''
output:

        *           

        * * *         

      * * * * *       

    * * * * * * *     

  * * * * * * * * *   

* * * * * * * * * * * 

* * * * * * * * * * * 

  * * * * * * * * *   

    * * * * * * *     

      * * * * *       

        * * *         

          *           

'''
