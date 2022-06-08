"""Defination: Program to Count Positive and Negative Numbers in Tuple """
def count_positive_negative(my_tuple):
    """algorithm to count positive or negative"""
    positive_count = negative_count = 0
    length_tuple=len(my_tuple)
    for i in range(length_tuple):
        if my_tuple[i] >= 0:
            positive_count = positive_count + 1
        else:
            negative_count = negative_count + 1
    print(f"The Count of Positive Numbers in posngTuple: {positive_count}")
    print(f"The Count of Negative Numbers in posngTuple: {negative_count}")
if __name__=='__main__':
    MY_TUPLE = (3, -22, -44, 19, -99, -37, 4, 11, -89)
    count_positive_negative(MY_TUPLE)
