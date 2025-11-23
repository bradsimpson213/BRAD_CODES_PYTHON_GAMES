

def print_display(board):
    b = board
    
    # create the board using a multi line string
    display = f""" 
            |       |
        {b[0]}   |   {b[1]}   |   {b[2]}   
     _______|_______|_______
            |       |
        {b[3]}   |   {b[4]}   |   {b[5]} 
     _______|_______|_______
            |       |
        {b[6]}   |   {b[7]}   |   {b[8]} 
            |       |
    """

    print(display)