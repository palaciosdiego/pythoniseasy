def advLoop(rows, cols):
    print("Rows: " + str(rows))
    print("Cols: " + str(cols))
    print("")
    term_size = terminal_size()

    if rows > term_size[0] or cols > term_size[1]:
        print("Your terminal size is " +
              str(term_size[0]) + " x " + str(term_size[1]))
        return False
    else:
        for row in range(1, rows+1):
            if not(row % 2 == 0):
                for col in range(1, cols+1):
                    if not(col % 2 == 0):
                        if col != cols:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        if col != cols:
                            print("|", end="")
                        else:
                            print("|")
            else:
                print("-"*cols)

        return True


def terminal_size():
    import fcntl
    import termios
    import struct
    h, w, hp, wp = struct.unpack('HHHH',
                                 fcntl.ioctl(0, termios.TIOCGWINSZ,
                                             struct.pack('HHHH', 0, 0, 0, 0)))
    return [h, w]


rows = int(input("Enter a number of rows: "))
cols = int(input("Enter a number of cols: "))
advLoop(rows, cols)
