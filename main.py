import functions
# This reads a line of input from stdin, strips any leading or trailing whitespace,
# and passes the resulting string to the count_pokemons function.
# The resulting count of caught pokemons is then printed to stdout.
movements = input().strip()
#Calls the function and send the movements
print(functions.count_pokemons(movements))


#Tests for more complex inputs
print("Tests:")
print(functions.count_pokemons("NNNNNNNEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNWWWWWWWWWWWWWWWWWWWWWWW"))
print(functions.count_pokemons("NNNNNNNNNNNNNNNNNNSSWWWWWWWWWWWWWEEEEEEEEESSSSSSSSSSS"))
print(functions.count_pokemons("SSSSSSSSSSSEEEEEEEEEEEWWWWWWWWWWWWNNNNNNNNNSSSSSSSSSSSSSSSSSN"))