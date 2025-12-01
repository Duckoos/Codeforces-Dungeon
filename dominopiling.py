m, n = map(int, input().split()) # dimensions of the board
pizza_size = 2 # because dimension of the pizza slice is 2 * 1 or 1 * 2
board_size = m * n

no_of_pizzas = int( board_size / pizza_size )
print(no_of_pizzas)


        