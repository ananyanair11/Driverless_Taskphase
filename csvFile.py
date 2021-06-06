f = open("namesNumbers.csv", "r")

#Sorting the rows with respect to the number
print("Sorted rows: ")
f = sorted(f, key = lambda x: int(x[0]))
s = []
for i in f:
    s.append(i.strip())
print(s)

#Modifying the rows by deleting the odd rows
del s[0::2]
print("After deleting the odd rows: ")
for i, line in enumerate(s):
    print(line)

#Storing all the names and trimming and trimming the spaces in a single string- strNames
strNames =""
for char in s:
    for i in range(len(char)):
        if (ord(char[i]) >= 65 and ord(char[i]) <= 90) or (ord(char[i]) >= 97 and ord(char[i]) <= 122):
            strNames += char[i]

print("All the names stored in a single string: ", strNames)

#Finding the minimum absolute ASCII difference in the string strNames
absDiff = 25
for i in range(len(strNames) - 2):
    for j in range(i + 1,len(strNames) - 1):    
        if abs(ord(strNames[i]) - ord(strNames[j])) < absDiff and strNames[i] != strNames[j]:
               absDiff = abs(ord(strNames[i]) - ord(strNames[j]))
               
print("The minimum absolute ASCII difference in the string is: ", absDiff)
