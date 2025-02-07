print("Let's count the number of permutations of rings in the Tower of Hanoi problem.")
a = int(input("Enter the number of disks: "))
the_tower = int(input("Enter the tower number to which the disks should be moved (1/2/3): "))

def towers(the_tower, a):
    if the_tower not in [1, 2, 3]:
        print("This is not possible under the given conditions of the problem")
    else:
        def rearrangement(a, spown, the_tower, secondary):
            while a > 0:
                rearrangement(a-1, spown, secondary, the_tower)
                print("Move disk", a, "from tower", spown, "to tower", the_tower)
                return rearrangement(a-1, secondary, the_tower, spown)
        spown = 1
        secondary = 2
        steps = 0
        for i in range(a):
            steps = steps*2 + 1
        rearrangement(a, spown, the_tower, secondary)

        print("Number of steps:", steps)

def repeat():
    i = 0
    while i < 1:
        repeat = input("Change the tower? (Yes/No)")
        repeat = repeat.lower()
        if repeat.startswith("y"):
            i += 1
            target  = int(input("Enter another tower: "))
            return towers(target, a)
        else:
            print("Have a nice day!")
            break

towers(the_tower, a)
repeat()
