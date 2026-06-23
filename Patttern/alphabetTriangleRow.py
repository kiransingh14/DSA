def alphabetTriangleRow(alphabet):
    for i in range(ord('A'), ord(alphabet)+1):
        for j in range(ord('A'), i+1):
           print(chr(i), end =" ")        
        print("\n")
alphabet = input("Enter alphabet:").upper()
alphabetTriangleRow(alphabet)

'''
output:

A 

B B 

C C C 

D D D D 

E E E E E 

F F F F F F 

G G G G G G G 
'''
