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
#matrix multiplication
multiplication_result=[]
for i in range(0,a):
    a1=[]
    for j in range(0,a):
        sum=0
        for k in range(0,a):
            sum=sum+m1[i][j]*m2[i][j]
        a1.append(sum)
    multiplication_result.append(a1)
print ("m1 x m2 =",multiplication_result)        
print('\n\nBy: MANASA J')
input('\nPress "manu" to Exit:-')
