import board

x = board.Board()

# x.place_new_set(0, 0, 1)
# x.place_new_set(0, 1, 1)
# x.place_new_set(0, 2, 1)
# x.place_new_set(1, 1, 1)

# x.display_board()

# print("")

# x.merge(0, 0, 0, 1)
# x.display_board()

playing = True
while x.can_win() and playing:
    print("")
    x.display_board()
    user_input = input("Enter Command (q, m, p): ")
    if user_input.lower() == "q":
        print("Goodbye!")
        playing = False
    elif user_input.lower() == "m":
        print(" ")
    elif user_input.lower() == "p":
        x.place_new_random()
        print("Place")
    else:
        print("Invalid Command")
        


