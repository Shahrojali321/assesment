"""Defination:Python program to check the parenthesis"""
def check_parentheses(paren):
    """Algorithm to check the balance of paren"""
    stack=[]
    bracket={'(':')','{':'}','[':']'}
    for char in paren:
        if char in ['(','{','[']:
            stack.append(char)
        else:
            if stack:
                top=stack.pop()
                if bracket[top]!=char:
                    return False
            else:
                return False
    return False if stack else True
if __name__=='__main__':
    PAREN=input("Enter the parenthesis combination: \n ")
    print(f"{check_parentheses(PAREN)}")
