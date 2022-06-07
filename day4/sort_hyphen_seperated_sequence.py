"""Defination:Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order"""
def sort_sequence(hyphen_sequence):
    """To sort the sequence"""
    sequence=hyphen_sequence.split('-')
    sequence.sort()
    return sequence
if __name__=='__main__':
    HYPHEN_SEQUENCE=input("Enter the hyphen seperated sequence: ")
    RESULT=sort_sequence(HYPHEN_SEQUENCE)
    print(f"The sorted hyphen seperated sequence is: {'-'.join(RESULT)}")
