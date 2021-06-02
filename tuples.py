#tupleInput
print("Enter the values of the tuple")
t =  tuple([eval(x) for x in input("Enter the values: ").split(',')])

#removing Duplicate Elements Of The Tuple
refer = []
modified = []
for i in t:
    if i not in refer:
        refer.append(i)
        modified.append(i)
        
print("The modified tuple after removing the duplicates is: ")
print(tuple(modified))

#sum Of Modified Tuple Using Recursion
t_sum = 0
def sumOfTuple(modified):
    global t_sum
    if len(modified) ==0 :
        return t_sum
    else:
        t_sum = t_sum + modified[0]
        modified = modified[1:]
        return (sumOfTuple(modified))
    
print("Sum of the modified tuple is: ")     
print(sumOfTuple(modified))
