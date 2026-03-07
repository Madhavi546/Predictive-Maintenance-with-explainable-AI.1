# Goal: create a list of squares for even numbers between 0 and 9

# Standard way (using loop)
square_loop = []
for x in range(10):
    if x % 2 == 0:
        square_loop.append(x**2)

# List comprehension way
squares_comp = [x**2 for x in range(10) if x % 2 == 0]

print(f"Loop version: {square_loop}")
print(f"Comprehension version: {squares_comp}")