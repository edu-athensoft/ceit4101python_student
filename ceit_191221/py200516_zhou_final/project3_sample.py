"""

"""


while True:
    print("=== Level 1 ===")
    cmd = input("Please enter level 1 menu \nnumber[1,2,3,4] \nor 'q' for exit: ")
    if cmd == 'q' or cmd == 'Q':
        break
    elif cmd in ['1','2','3','4']:
        print("Lvl 1 Menu: {} selected".format(cmd))
        # call level 2 menu program
        while True:
            print("=== Level 2 ===")
            cmd2 = input("Enter level 2 menu \nnumber[1,2,3] \nor 'q' for exit to Level 1: ")
            if cmd2 =='q' or cmd2 == 'Q':
                break
            elif cmd2 in ['1','2','3']:
                print("input number")
                print("converting")
                print("show result")
            else:
                print("Invalid input")
            print("\n\n")
    else:
        print("Invalid input")
    print("\n\n")
