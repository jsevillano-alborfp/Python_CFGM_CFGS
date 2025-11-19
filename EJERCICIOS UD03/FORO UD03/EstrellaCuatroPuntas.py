size = 9

for i in range(size):
    for j in range(size):
        if i == size // 2 or j == size // 2 or i == j or i + j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
