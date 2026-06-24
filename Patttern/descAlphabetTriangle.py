def descAlphabetTriangle(n):
    for i in range(n):            
        for k in range(i, -1, -1):
            print(chr(ord('A')+n-k-1), end=" ")
        
        print()
number = int(input("Enter number:"))
descAlphabetTriangle(number)

'''
output:
    
E 
D E 
C D E 
B C D E 
A B C D E 

'''