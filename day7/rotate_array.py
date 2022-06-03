"""deefination: Python Program for array rotation"""
def rotate_array(array,number):
    """algorithm to rotate the array"""
    array[:]=array[number:] + array[:number] 
    return array
    
"""calling the function"""
if __name__=='__main__':
    array=[1,2,3,4,5,6,7]
    number=int(input("Enter the step from which it rotate: "))
    print(f"The rotated array is : {rotate_array(array,number)}")