def butterflyStars(number):
    for i in range(number):
        for _ in range(number-i):
            print("*", end =" ")
        for _ in range(0,2*i):
            print(" ", end =" ")
        for _ in range(number-i):
            print("*", end =" ")
        print("\n")
    for j in range(number):
        for _ in range(j+1):
            print("*", end =" ")
        for _ in range(2*(number-j)-2):
            print(" ", end =" ")
        for _ in range(j+1):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
butterflyStars(number)


'''
output:
* * * * * * * * * * 

* * * *     * * * * 

* * *         * * * 

* *             * * 

*                 * 

*                 * 

* *             * * 

* * *         * * * 

* * * *     * * * * 

* * * * * * * * * * 

'''
