"""defination:To convert the Snake notation to Pascel notation"""
    
def snake_case(str):
    """To convert the Snake notation to Pascel notation"""
    sc=str.split("_")
    for word in range(len(sc)):
        sc[word]=sc[word].capitalize()
    return "".join(sc)

if __name__=='__main__':

    input=input("Enter the snake_case: ")
    print(f"Pascel case is: {snake_case(input)} ")