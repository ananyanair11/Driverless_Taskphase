#charachter List Input
print("Enter the characters of the list separated by a comma :")
inputString = input()
characterList = inputString.split(',')

#function To Check For Palindrome
def isPalindrome(c, i, j):
    if i == j or j < i:
        return True
    elif c[i] != c[j]:
        return False
    else:
        return isPalindrome(c, i + 1, j - 1)

#fucntion To Print Hex Values   
def convert_to_hex(c):
    hex_values = [hex(ord(character))[2:] for character in c]
    print(hex_values)

#fucntion To Print Diamond Pattern
def print_pattern(c):
    row = len(c)
    for i in range(1, row+1):
        for j in range(1, row-i+1):
            print(' ', end = ' ')
        for j in range(1,i+1):
            print(c[j-1], end = ' ')
        for j in range(i-1,0,-1):
            print(c[j-1], end = ' ')
        print()
    for i in range(row-1,0,-1):
        for j in range(1,row-i+1):
            print(' ', end=' ')
        for j in range(1,i+1):
            print(c[j-1], end = ' ')
        for j in range(i-1,0,-1):
            print(c[j-1], end = ' ')
        print()
        
ans = isPalindrome(characterList, 0, len(characterList) - 1)

if ans == True:
    print("The list is a Palindrome")
    convert_to_hex(characterList)
else:
    print("The list is not a Palindrome")
    print_pattern(characterList)
