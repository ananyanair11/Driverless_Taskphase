class operations:
    def __init__(op, C = []):
        op.C = C
        
    def calc_det(C, Amat):
        finalAnswer = 0
        A = Amat
        answer2x2 = 0
        #Determinant value calculation for 2X2 determinant
        if len(A) == 2 and len(A[0]) == 2:
           answer2x2 = A[0][0] * A[1][1] - A[1][0] * A[0][1]
           return answer2x2
    
        #Determinant value calculation for nxn determinant 
        for column in range(len(A)): 
            nestedDet = A 
            nestedDet = nestedDet[1:]
        
            for i in range(len(nestedDet)): 
                nestedDet[i] = nestedDet[i][0:column] + nestedDet[i][column+1:]
               
            if column % 2 == 0:
                sign = 1
            else:
                sign = -1
            
            finalAnswer += sign * A[0][column] * C.calc_det(nestedDet)
     
        return finalAnswer
    
    def calc_adj(C, Amat):
        sign = -1
        A = Amat
        def calc_minor(m,i,j):
            return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
        
        cofactors = []
        for r in range(len(A)):
            cofactorRow = []
            for c in range(len(A)):
                minor = calc_minor(A,r,c)
                if sign == 1:
                   sign = -1
                elif sign == -1:
                     sign = 1
                cofactorRow.append(sign * C.calc_det(minor))
            cofactors.append(cofactorRow)
        return cofactors    

    def calc_inv(C, Amat):
        determinant = 0
        A = Amat
        determinant = C.calc_det(A)
        if determinant > 0:
           cofactors = C.calc_adj(A)
           inverse = []
           for r in range(len(A)):
               row = []
               for c in range(len(A)):
                   row.append(cofactors[r][c]/determinant)
               inverse.append(row)
                    
           return inverse
        else:
           print("Inverse does not exist for:", A)
           return -1
