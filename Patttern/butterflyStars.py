def halfedDiamondStars(number):
    for i in range(0,number):
        for _ in range(0, i+1):
            print("*", end =" ")
        for _ in range(2*(number-i)-2):
            print(" ", end =" ")
        for _ in range(i+1):
            print("*", end =" ")
        print("\n")
    for i in range(1,number):
        for _ in range(0,number-i):
            print("*", end =" ")
        for _ in range(0,2*i):
            print(" ", end =" ")
        for _ in range(0,number-i):
            print("*", end =" ")
        print("\n")
number = int(input("Enter number:"))
halfedDiamondStars(number)