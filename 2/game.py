# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    global field
    global field_origin
    field = list(range(1,16))
    field += EMPTY_MARK
    field_origin = tuple(field)
    random.shuffle(field)

def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    i = 0
    for tile in field:
    	i += 1
    	if i % 4 == 0:
    		print(tile)
    	else:
    		#превращаем list в поле 4x4
    		print(tile, ' ', end='')
    print('\n')
#    return None

def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if tuple(field) == field_origin:
        return True
    else:
        return False

def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    oldindex = field.index(EMPTY_MARK)
    move = (MOVES[key])
    if move < 0:
        newindex = oldindex - -move
    else:
        newindex = oldindex + move
    if oldindex in (0, 4, 8, 12) and (move == -1):
    	raise IndexError
    elif oldindex in (3, 7, 11, 15) and (move == 1):
    	raise IndexError
    else:
        field[newindex], field[oldindex] = field[oldindex], field[newindex]
        return field

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    key = input()
    return key

def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    steps = 0
    shuffle_field()
    print_field(field)
    print('Your step! a, w, s, d:')
    while not is_game_finished(field):
        oldindex = field.index(EMPTY_MARK)
        try:
            perform_move(field, handle_user_input())
        except IndexError:
        	print('Oops! You can\'t exit from borders \n' )
        print_field(field)
        print('\nYour next step: ')
        steps += 1
    else:
        print('Done! Steps: ', steps)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    try:
        main()
    except KeyboardInterrupt:
        print('\nshutting down') 





