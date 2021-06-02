#Inputs for matrix A
print("For matrix A")
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

A = []
print("Enter the entries rowwise:")

for i in range(R):		 
	row =[]
	for j in range(C):	 
		row.append(int(input()))
	A.append(row)

#Inputs for matrix B
print("For matrix B")
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

B = []
print("Enter the entries rowwise:")

for i in range(r):		 
	row =[]
	for j in range(c):	 
		row.append(int(input()))
	B.append(row)

#Multiplication of matrices A and B
print(" (a)MULTIPLICATION OF TWO MATRICES ")
if C != r:
  print("Invalid entry. Number of columns of A must be equal to number of rows of B")
  quit()
else:
  m_result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]   

print("A x B is ")
for m in m_result:
    print(m)

#Transpose of AB
print("(b) TRANSPOSE OF MATRIX ")
AB_transpose = [[m_result[j][i] for j in range(len(m_result))] for i in range(len(m_result[0]))]
print(" (AB) transpose is: ")
for t in AB_transpose:
    print(t)

#Transpose of matrrix A
print(" A transpose is ")
A_transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for t in A_transpose:
    print(t)

#Transpose of matrix B
print(" B transpose is ")
B_transpose = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
for t in B_transpose:
    print(t)
      
# B transpose * A Transpose
t_result = [[sum(a*b for a,b in zip(B_transpose_row,A_transpose_col)) for A_transpose_col in zip(*A_transpose)] for B_transpose_row in B_transpose]
print( "B^T * A^T IS ")
for t in t_result:
    print(t)

#Verification
print(" (c) VERICATION ")
y = (sorted(AB_transpose) == sorted(t_result))
if y == True:
  print("(AB)tranpose and B^T*A^T are Equal")
  print("Hence proved")

      
