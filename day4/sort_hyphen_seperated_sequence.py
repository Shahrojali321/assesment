"""Defination:Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order"""

def sort_sequence(hyphen_sequence):
    """To sort the sequence"""
    sequence=hyphen_sequence.split('-')
    sequence.sort()

    return sequence
    
hyphen_sequence=input("Enter the hyphen seperated sequence: ")
sorted_sequence=sort_sequence(hyphen_sequence)
print(f"The sorted hyphen seperated sequence is: {'-'.join(sorted_sequence)}")