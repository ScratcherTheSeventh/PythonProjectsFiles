import numpy

def run():
    chestnum, victornum = [], []
    usrchst = int(input("Chest amount that you want to find the winning chests of >>> "))
    if usrchst == 0:
        print("Not a Number")
        run()
    anchor1, anchor2 = 1, 2 

    for i in range(usrchst):
        if anchor1 == anchor2:
            anchor1 = 1
        victornum.append(anchor1)
        chestnum.append(anchor2)
        anchor2 += 1
        anchor1 += 2

    victornum.append(int(victornum[-1] + 2))
    victornum.pop(0)
    victornum.insert(0, 1)
    chestnum.insert(0, 1)

    print(f"For {usrchst} people, person #{victornum[-2]} will survive")

while True:
    run()
