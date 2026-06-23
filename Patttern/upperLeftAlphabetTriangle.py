def upperLeftAlphabetTriangle(alphabet):
    end = ord(alphabet)
    for i in range(end, ord('A') - 1, -1):
        for j in range(ord('A'), i + 1):
            print(chr(j), end=" ")
        print()
alphabet = input("Enter alphabet:").upper()
upperLeftAlphabetTriangle(alphabet)

'''
output:
A B C D E F G 
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
'''