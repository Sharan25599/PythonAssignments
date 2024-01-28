def insert_character(string, character, position):

    if position < 0 or position >= len(string):
        raise IndexError("Invalid position for character insertion.")

    return string[:position] + character + string[position:]
