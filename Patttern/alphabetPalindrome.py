def alphabetPalindrome(n):    
    for i in range(n):
        for _ in range(n-i-1):
            print(" ", end=" ")
        
        for j in range(i+1):
            print(chr(ord('A')+j), end=" ")
            
        for k in range(i-1, -1, -1):
            print(chr(ord('A')+k), end=" ")
        
        for _ in range(n-i-1):
            print(" ", end=" ")
        print()
number = int(input("Enter number:"))
alphabetPalindrome(number)


'''

output :
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
'''
