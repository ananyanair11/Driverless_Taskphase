Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1
2
3
1 
2 
3 
1 
2 
3 
>>> 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1 2 3 4 5 6
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 10, in <module>
    a.append(int(input()))
ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6'
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1
2
3
1 
2 
3 
1 
2 
3 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1
2
3
4
5
6
1 
2 
3 
1 
2 
3 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1
2
3
4
5
6
1 
2 
3 
1 
2 
3 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the matirx rowwise
1
2
3
4
5
6
1 2 3 1 2 3 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
1 2 3 
4 5 6 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
1 2 3 
4 5 6 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
1 2 3 
4 5 6 
For matrix B
Enter the number of rows:4
Enter the number of columns:2
Enter the entries rowwise:
1
2
3
4
5
6
7
8
1 2 
3 4 
5 6 
7 8 
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
1
1
1
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 31, in <module>
    for j in range(len(A[0])):
TypeError: object of type 'int' has no len()
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
1
1
1
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 30, in <module>
    result = [[sum(x*y for x,y in zip(a_row,A_col)) for A_col in zip(*A)] for a_row in a]
  File "/home/ananya/Desktop/matrix.py", line 30, in <listcomp>
    result = [[sum(x*y for x,y in zip(a_row,A_col)) for A_col in zip(*A)] for a_row in a]
TypeError: zip argument #1 must support iteration
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
1
1
1
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 30, in <module>
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
  File "/home/ananya/Desktop/matrix.py", line 30, in <listcomp>
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
TypeError: zip argument #1 must support iteration
>>> 
================== RESTART: /home/ananya/Desktop/random.py ==================
[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
For matrix B
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 30, in <module>
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
  File "/home/ananya/Desktop/matrix.py", line 30, in <listcomp>
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
TypeError: zip argument #1 must support iteration
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
For matrix B
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
[1]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
1
1
1
[3, 3, 3]
[3, 3, 3]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
3
3
1
2
3
4
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 30, in <module>
    m_result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for X_row in X]
NameError: name 'X' is not defined
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
1
1
1
1
1
1
1
1
[3, 3, 3]
[3, 3, 3]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
For matrix B
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
1
[1]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
3
3
3
3
3
3
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
2
2
2
2
2
2
2
2
2
[18, 18, 18]
[18, 18, 18]
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 39, in <module>
    A_transpose = [[A[i][j] for j in range(len(A))] for i in range(len(A[0]))]
  File "/home/ananya/Desktop/matrix.py", line 39, in <listcomp>
    A_transpose = [[A[i][j] for j in range(len(A))] for i in range(len(A[0]))]
  File "/home/ananya/Desktop/matrix.py", line 39, in <listcomp>
    A_transpose = [[A[i][j] for j in range(len(A))] for i in range(len(A[0]))]
IndexError: list index out of range
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
3
3
3
3
3
3
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
3
3
3
3
3
3
3
3
3
[27, 27, 27]
[27, 27, 27]
[3, 3]
[3, 3]
[3, 3]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
A x B is 
[30, 36, 42]
[66, 81, 96]
 (AB) transpose is: 
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 43, in <module>
    for t in AB_transpose:
NameError: name 'AB_transpose' is not defined
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
A x B is 
[30, 36, 42]
[66, 81, 96]
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
B^T * A^T is 
[30, 66]
[36, 81]
[42, 96]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
3
2
1
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[18, 24, 30]
[66, 81, 96]
(b) TRANSPOSE OF A MATRIX 
 (AB) transpose is: 
[18, 66]
[24, 81]
[30, 96]
 A transpose is 
[3, 4]
[2, 5]
[1, 6]
 b transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T is 
[18, 66]
[24, 81]
[30, 96]
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 65, in <module>
    if range(len(m_result)) == range(len(t_result)) & range(len(m_result[0])) == range(len(t_result[0])):
TypeError: unsupported operand type(s) for &: 'range' and 'range'
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 3, in <module>
    R = int(input("Enter the number of rows:"))
ValueError: invalid literal for int() with base 10: ''
>>> 3
3
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF A MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 b transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T is 
[30, 66]
[36, 81]
[42, 96]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
Not equal
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 68, in <module>
    if AB_transpose[i][j] == t_result[i][j]:
TypeError: list indices must be integers or slices, not list
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
True
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:2
Enter the entries rowwise:
3
1
For matrix B
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[7, 11, 15]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[7]
[11]
[15]
 A transpose is 
[3]
[1]
 B transpose is 
[1, 4]
[2, 5]
[3, 6]
B^T * A^T IS 
[7]
[11]
[15]
7
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
True
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
t
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
A x B is 
[30, 36, 42]
[66, 81, 96]
(b) TRANSPOSE OF MATRIX 
 (AB) transpose is: 
[30, 66]
[36, 81]
[42, 96]
 A transpose is 
[1, 4]
[2, 5]
[3, 6]
 B transpose is 
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
B^T * A^T IS 
[30, 66]
[36, 81]
[42, 96]
 (c) VERICATION 
(AB)tranpose and B^T*A^T are Equal
Hence proved
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:1
Enter the entries rowwise:
3
For matrix B
Enter the number of rows:4
Enter the number of columns:2
Enter the entries rowwise:
3
3
3
3
3
3
2
1
 (a)MULTIPLICATION OF TWO MATRICES 
Invalid entry. Number of columns of A must be equal to number of rows of B
A x B is 
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 37, in <module>
    for m in m_result:
NameError: name 'm_result' is not defined
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:5
Enter the entries rowwise:
1
2
3
4
5
For matrix B
Enter the number of rows:7
Enter the number of columns:9
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0
exit()
Traceback (most recent call last):
  File "/home/ananya/Desktop/matrix.py", line 26, in <module>
    row.append(int(input()))
ValueError: invalid literal for int() with base 10: 'exit()'
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:1
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
For matrix B
Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
 (a)MULTIPLICATION OF TWO MATRICES 
Invalid entry. Number of columns of A must be equal to number of rows of B
>>> 
================== RESTART: /home/ananya/Desktop/matrix.py ==================
For matrix A
Enter the number of rows:2
Enter the number of columns:1
Enter the entries rowwise:
1
1
For matrix B
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
 (a)MULTIPLICATION OF TWO MATRICES 
Invalid entry. Number of columns of A must be equal to number of rows of B
>>> 
