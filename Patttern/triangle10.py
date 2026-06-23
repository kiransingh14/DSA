def triangle10(number):
    for i in range(1,number+1):
        if(i%2==0):
            start=0
        else:
            start=1   
        for _ in range(1, i+1):
           print(start, end =" ")
           start =1-start
        
        print("\n")
number = int(input("Enter number:"))
triangle10(number)


'''
output:
1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1 

0 1 0 1 0 1 
'''
