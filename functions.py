def count_pokemons(movements):
    #create a set since it is an unordered collection and it cannot contain duplicated elements
    visited = set()
    #variables for coordinates, Y for north and south, x for east and west
    x, y = 0, 0
    # counter for the number of pokemons caught
    count = 0
    # a for cycle to go through the movements that were given
    for move in movements:
        #if the move at the current position correspond to N, we will add 1 position at Y
        if move == 'N' or move =='n':
            y += 1
        # if the move at the current position correspond to S, we will remove 1 position at Y
        elif move == 'S' or move =='s':
            y -= 1
        # if the move at the current position correspond to E, we will add 1 position at X
        elif move == 'E' or move =='e':
            x += 1
        # if the move at the current position correspond to O, we will remove 1 position at Y
        elif move == 'O' or move =='o':
            x -= 1
        #this is a tuple, an ordered collection and unchangeable collection in python, in this case i will use it to store, we can use a list for this purpose but for it seems that a tuple is a little more efficient
        pos = (x, y)
        #check if the position was not visited
        if pos not in visited:
            #if is not, we will add the position (X and Y) to the visited set, so it will not be repeated
            visited.add(pos)
            #add to the counter another pokemon
            count += 1

    return count
