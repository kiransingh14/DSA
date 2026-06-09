def checkGrading(mark):
    if (mark < 25):
        print("F")
    elif(mark <= 44):
        print("E")
    elif(mark <=49):
        print("D")
    elif(mark <= 59):
        print("C")
    elif(mark  <= 79):
        print("B")
    elif(mark <= 100):
        print("A")
    else:
        print("Not defined")
mark = int(input("Enter your marks:"))
checkGrading(mark)
