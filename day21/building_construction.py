"""Defination:Program to count the number of ways to construct the building"""
def count_ways(plots):
    """Algorithm"""
    if plots==1:
        return 4
    else:
        count_building=1
        count_spaces=1
        for plot in range(2,plots+1):
            previous_count_building=count_building
            previous_count_spaces=count_spaces
            count_spaces=previous_count_building+previous_count_spaces
            count_building=previous_count_spaces
        result=(count_spaces+count_building)*(count_spaces+count_building)
    return result
if __name__=='__main__':
    PLOTS=int(input("Enter the number of plots: "))
    print(f"The number of ways that plot can be made : \n {count_ways(PLOTS)}")
