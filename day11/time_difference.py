"""Defination:Program to find difference between current time and given time"""
def difference(hour1, minute1, hour2, minute2):
    """algorithm to find difference"""
    time1 = hour1 * 60 + minute1
    time2 = hour2 * 60 + minute2
    if time1 == time2:
        print("Both are same times")
        return
    else:
        diff = time2-time1
    hour_difference = int(diff / 60)
    minute_diffence = diff % 60
    print(hour_difference, ":", minute_diffence)
if __name__ == "__main__":
    HOUR1=int(input("Enter the hour of 1st time: "))
    MINUTE1=int(input("ENter the minute of 1st time: "))
    print(f"1st time is : \n {HOUR1}:{MINUTE1}")
    HOUR2=int(input("Enter the hour of 2nd time: "))
    MINUTE2=int(input("enter the minute of 2nd time : "))
    print(f"2nd time is: {HOUR2}:{MINUTE2} ")
    difference(HOUR1,MINUTE1,HOUR2,MINUTE2)
