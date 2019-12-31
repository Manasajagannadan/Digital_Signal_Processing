#matrix multiplication
#print the statement
print("MATRIX MULTIPLICATIN")
print("\nBY MANU")
#giving instructions for matrix statement
print("\nenter the no.of rows x columns:-")
#giving the form in integer
a=int(input())
#assuming that two matrices as empty arrayfor to store the elements
m1=[]
m2=[]
#statement to enter the matrix 1st one
print("\nenter the numbers in 1st matrix:-")
for i in range(0,a):
    print("\nenter the matrix column given by the nxn matrix",i)
    p=list(map(int,input().split()))
    m1.append(p)
print("\nthe 1st matrix is:",m1)
#statement to enter the matrix 2nd one
print("\nenter the number in 2nd matrix:-")
for j in range(0,a):
    print("\nenter the matrix column given by the nxn matrix",j)
    q=list(map(int,input().split()))
    m2.append(q)
print("\nthe 2nd matrix is:",m2)
#transpose of a matrix 
transpose_matrix_result1=[]
#transpose_matrix_result2=[]
for i in range(0,a):
    a1=[]
#    a2=[]
    for j in range(0,a):
        a1.append(m1[j][i])
    transpose_matrix_result1.append(a1)       
#        a2.append(m2[j][i])
#    transpose_matrix_result2.append(a2) 
print("\ntranspose matrix:-",transpose_matrix_result1)  
#print("\ntranspose matrix:-",transepose_matrix_result2)      
print('\n\nBy: MANASA J')
input('\nPress "manu" to Exit:-')
