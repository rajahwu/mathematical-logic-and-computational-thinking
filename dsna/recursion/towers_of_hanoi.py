def towers_of_hanoi(number_of_disks, start_peg, end_peg):
    if number_of_disks:
        towers_of_hanoi(number_of_disks - 1, start_peg, 6 - start_peg - end_peg)
        print(f"Move disk {number_of_disks} from peg {start_peg} to peg {end_peg}")
        towers_of_hanoi(number_of_disks - 1, 6 - start_peg - end_peg, end_peg)
        
towers_of_hanoi(3, 1, 3)