import matrix_operation

print("Enter n")
n = int(input())

print("Enter the details for matrix A")
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

print("Enter the details for matrix B")

B = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

o = matrix_operation.operations()
p = matrix_operation.operations()
A_inv = o.calc_inv(A)
B_inv = p.calc_inv(B)

if B_inv != -1:
    print(" (a) A x (INVERSE(B) IS : ")
    m_result = [[sum(a*b for a,b in zip(A_row,B_inv_col)) for B_inv_col in zip(*B_inv)] for A_row in A]
    for m in m_result:
        print(m)
    if A_inv != -1:
       print(" (b) INVERSE(A) x INVERSE(B)")
       n_result = [[sum(a*b for a,b in zip(A_inv_row,B_inv_col)) for B_inv_col in zip(*B_inv)] for A_inv_row in A_inv]
       for n in n_result:
           print(n)

