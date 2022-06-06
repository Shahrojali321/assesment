"""Defination:Program to Transpose a matrix in Single line"""
def transpose_of_matrix(matrix):
    """program to find transpose"""
    for row in matrix :
        print(row)
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("\n")
    print("The transpose matrix is : ")
    for row in transposed_matrix:
        print(row)
if __name__=='__main__':
    matrix1=[[4,5,6],[9,0,4],[8,7,3]]
    transpose_of_matrix(matrix1)
