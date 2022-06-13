"""Defination:To find Addition of two matrix"""
def matrix(matrix_row,matrix_column):
    """To find Addition of two matrix"""
    outer_matrix = []
    for i in range(1,matrix_row+1):
        row = []
        for j in range(1,matrix_column+1):
            elements = int(input(f"Enter outer_matrix[{i}][{j}] : "))
            row.append(elements)
        outer_matrix.append(row)
    return outer_matrix
def sum_and_subs(matrix1,matrix2):
    """algorithm for addition and substraction"""
    addition = []
    substraction=[]
    for i in range(len(matrix1)):
        row1 = []
        row2=[]
        for j in range(len(matrix1[0])):
            row1.append(matrix1[i][j] + matrix2[i][j])
            row2.append(matrix1[i][j]-matrix2[i][j])
        addition.append(row1)
        substraction.append(row2)
    print(f"The addition of matrix is : \n {addition}")
    print(f"The substraction of matrix is : \n {substraction}")
if __name__=='__main__':
    MATRIX_ROW=int(input("Enter the number of rows: \n"))
    MATRIX_COLUMN=int(input("Enter the number of colums: \n"))
    print("Enter the matrix1")
    MATRIX1=matrix(MATRIX_ROW,MATRIX_COLUMN)
    print(f"1st matrix is : \n {MATRIX1}")
    print("Enter the matrix2")
    MATRIX2=matrix(MATRIX_ROW,MATRIX_COLUMN)
    print(f"The 2nd matrix is: {MATRIX2}")
    sum_and_subs(MATRIX1,MATRIX2)
