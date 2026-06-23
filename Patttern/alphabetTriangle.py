def alphabetTriangle(alphabet):
    for i in range(ord('A'), ord(alphabet)+1):
        for j in range(ord('A'), i+1):
           print(chr(j), end =" ")        
        print("\n")
alphabet = input("Enter alphabet:").upper()
alphabetTriangle(alphabet)


'''
output:
A 

A B 

A B C 

A B C D 

A B C D E 

A B C D E F 
'''
