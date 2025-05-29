#!/usr/bin/python3

def draw_square_pattern():
    size = int(input("Enter the size of the pattern: "))
    
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # new line after each row
        row += 1

if __name__ == "__main__":
    draw_square_pattern()
