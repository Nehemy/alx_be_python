size = int(input("Enter the size of the pattern: "))

square = 0

while square != size:
    for i in range(1, size + 1):
        print("*", end="")
    print()
    square += 1
    