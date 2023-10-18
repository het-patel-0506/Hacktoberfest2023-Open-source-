class Array2D:
    def _init_(self):
        return
    def Matrix(self,R,C):
        self.row=R
        self.col=C
        self.matrix=[0]*R
        for i in range(R):
            self.matrix[i]=[0]*C
        
    def Rows(self):
        return self.row
    
    def Cols(self):
        return self.col
    
    def prn2d(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
            
    def getitem(self,i1,j1) :
        for i in range (len(self.row)):
            if(i==i1) :
                for j in range (len(self.col)):
                    if(j==j1) :
                        A=self.row[i][j]
                        return A
            
    def setitem(self,i,j,value):
        if(self.row>=i and self.col>=j):
            self.matrix[i-1][j-1]=value
        else:
            print("!!! Invalid Position!!!")
            
            
    def Gen_Spar(self):
        self.Gen_Spar=[]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if(self.matrix[i][j]!=0):
                    self.Gen_Spar.append([i,j,self.matrix[i][j]])
                    
    def S_setitem(self,a,b,value):
        flag=0
        if(a<=self.row and b<=self.col):
            for i in range(len(self.Gen_Spar)):
                if (self.Gen_Spar[i][0]==(a) and self.Gen_Spar[i][1]==(b)):
                    self.Gen_Spar[i][2]=value
                    flag=1
                    break
            if(flag!=1):
                self.Gen_Spar.append([a,b,value])
            # print("Value added ")
        else:
            print("!!!Index out of range!!!")
        print("Value added")
        print()
        
    def Sacling(self,value):
        for i in range(len(self.Gen_Spar)):
            self.Gen_Spar[i][2]*=value
        print("Matrix updated.")
        
    def Trans(self):
        for i in range(len(self.Gen_Spar)):
            temp=self.Gen_Spar[i][0]
            self.Gen_Spar[i][0]=self.Gen_Spar[i][1]
            self.Gen_Spar[i][1]=temp
        print("The Matrix has been Transposed.")
        
    def add(self,matrixrhs):
        for j in range(len(matrixrhs)):
            flag=0
            for i in range(len(self.Gen_Spar)):
                if(self.Gen_Spar[i][0]==matrixrhs[j][0] and self.Gen_Spar[i][1]==matrixrhs[j][1]):
                    self.Gen_Spar[i][2]+=matrixrhs[j][2]
                    flag=1
                    break
            if(flag==0):
                self.Gen_Spar.append(matrixrhs[j])
        for j in range(len(self.Gen_Spar)) :
            if (self.Gen_Spar[j][2]==0) :
                self.Gen_Spar.pop(j)
                    
                    
    def sub(self,matrixrhs):
        for j in range(len(matrixrhs)):
            flag=0
            for i in range(len(self.Gen_Spar)):
                if(self.Gen_Spar[i][0]==matrixrhs[j][0] and self.Gen_Spar[i][1]==matrixrhs[j][1]):
                    self.Gen_Spar[i][2]-=matrixrhs[j][2]
                    flag=1
                    break
            if(flag==0):
                    matrixrhs[j][2]=-(matrixrhs[j][2])
                    self.Gen_Spar.append(matrixrhs[j])

        for j in range(len(self.Gen_Spar)) :
            if (self.Gen_Spar[j][2]==0) :
                self.Gen_Spar.pop(j)
                    
    def Sprn2d(self):
        for i in range(len(self.Gen_Spar)):
            print(self.Gen_Spar[i])
            
    def Return_M(self) :
        return self.Gen_Spar
            
            
            
A=Array2D()
A.Matrix(5,6)
A.setitem(0,0,5)
A.setitem(1,1,5)
A.setitem(2,3,9)
A.setitem(5,6,8)

print("Number of the Rows : ",A.Rows())
print("Number of the Column : ",A.Cols())
A.setitem(1,0,3)
A.setitem(2,3,56)

A.prn2d()
print()
#Sparse Matrix
A.Gen_Spar()
A.Sprn2d()
print()
A.S_setitem(2,3,1)
A.Sprn2d()
print()
A.Sacling(2)
A.Sprn2d()
print()
# A.Trans()
# A.Sprn2d()
print()

# Second matrix
A2=Array2D()
A2.Matrix(5,6)
A2.Gen_Spar()
A2.S_setitem(0,0,15)
A2.S_setitem(2,4,10)
A2.S_setitem(4,5,10)
A2.Sprn2d()
print()
A5=A2.Return_M()
A3=A2.Return_M()
print()
A.add(A5)
A.Sprn2d()

print()
print()
A.sub(A3)
A.Sprn2d()
