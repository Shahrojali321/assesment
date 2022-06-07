"""defination:To convert the Snake notation to Pascel notation"""
def snake_case(string1):
    """To convert the Snake notation to Pascel notation"""
    string=string1.split("_")
    for word in range(len(string)):
        string[word]=string[word].capitalize()
    return "".join(string)
if __name__=='__main__':
    INPUT=input("Enter the snake_case: ")
    print(f"Pascel case is: {snake_case(INPUT)} ")
