"""Defination: Program for Heap Sort"""
def heap_sort(list1):
    """Algorithm for heap sort"""
    for j in range((len(list1)-2)//2,-1,-1):
        sift_down(list1,j,len(list1))
    for end in range(len(list1)-1,0,-1):
        swap_list(list1,0,end)
        sift_down(list1,0,end)

def sift_down(list1,i,upper):
    """algorithm to sift the number"""
    while True:
        left,rigth=i*2+1, i*2+2
        if max(left,rigth)<upper:
            if list1[i]>=max(list1[left],list1[rigth]):
                break
            elif list1[left] > list1[rigth] :
                swap_list(list1,i,left)
                i = left
            else:
                swap_list(list1,i,rigth)
                i = rigth
        elif left < upper:
            if list1[left] > list1[rigth]:
                swap_list(list1,i, left)
                i = left
            else: break
        elif rigth < upper :
            if list1[rigth] > list1[left]:
                swap_list(list1,i,rigth)
                i=rigth
            else:break
        else: break

def swap_list(list1,i,j):
    """for swap"""
    list1[i],list1[j]=list1[j],list1[i]

if __name__=='__main__':
    LIST1=[]
    list_length=int(input("Enter the list length: "))
    for element in range(0,list_length):
        element=int(input("Enter the element of list: "))
        LIST1.append(element)
    print(LIST1)
    heap_sort(LIST1)
    print(f"The sorted list is : \n {LIST1}")
