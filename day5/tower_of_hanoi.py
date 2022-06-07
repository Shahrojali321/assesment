"""Defination: Program for Tower of Hanoi puzzle """
def hanoi_tower(disk,start,auxiliary,end):
    """ function to solve the puzzle """
    if disk==1:
        print(f"Move dist 1 from rod {start} to rod {end}")
        return
    hanoi_tower(disk-1,start,end,auxiliary)
    print(f"Move disk {disk} from rod {start} to rod {end}")
    hanoi_tower(disk-1,auxiliary,start,end)
if __name__=='__main__':
    DISK=int(input("Enter the number of disk: "))
    hanoi_tower(DISK,"A","B","C")
