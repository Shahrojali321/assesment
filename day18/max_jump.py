"""Defination:Program to find the number of jump to reach the end """
def min_jumps(arr, arr_length):
    """Algorithm to get the jumps"""
    jumps = [0 for i in range(arr_length)]
    for i in range(arr_length-1, -1, -1):
        if arr[i] == 0:
            jumps[i] = float('inf')
        elif arr[i] >= arr_length - i - 1:
            jumps[i] = 1
        else:
            minimum = float('inf')
            for j in range(i + 1, arr_length):
                if j <= arr[i] + i:
                    if minimum > jumps[j]:
                        minimum = jumps[j]
            if minimum != float('inf'):
                jumps[i] = minimum + 1
            else:
                jumps[i] = minimum
    return jumps[0]
if __name__=='__main__':
    ARR=[]
    ARR_LENGTH = int(input("Enter the length of array: "))
    for element in range(ARR_LENGTH):
        elements=int(input("Enter the element: of array: \n"))
    ARR.append(elements)
    print('Minimum number of jumps to reach',
        'end is', min_jumps(ARR, ARR_LENGTH))
