import pprint


text = input("Enter your text with an even number of letters: ")

# Keep only the even-indexed letters
result = text[::2]
print(result)

# Reverse the last half of the string
mid = len(result) // 2
result = result[:mid] + result[mid:][::-1]
print(result)

# Swap the first and last letters of the string
result = result[-1] + result[1:-1] + result[0]

# Print the encoded message in uppercase
print(result.upper())
#making a sperator line between tasks 
print(" __________________________________________________________________________ ")
"""Write a Python program that does the following:
Ask the user to enter any number of product
prices in one line, separated by spaces.
Loop through the prices using a for loop.
Use if, elif, and else to check the value of
each price and print its category.
– between 0 and 50 > cheap
– between 50 and 100 > mid
– greater than 100 > expensive"""
pricewds = input("Enter product prices separated by spaces: ")
prices = pricewds.split() 
for price in prices:
    price = float(price)  # Convert the price to a float for comparison
    if 0 < price <= 50:
        print(f"{price} is cheap")
    elif 50 < price <= 100:
        print(f"{price} is mid")
    elif price > 100:
        print(f"{price} is expensive")
    else:
        print(f"{price} is not a valid price")
pprint.pprint(" __________________________________________________________________________ ")
'''Exercise: "Matrix"
1 0 2  
0 3 0  
2 0 1  
1.Create a 3x3 grid initialized with zeros.
2.Fill the grid such that:
3.The main diagonal (top-left to bottom-right)
contains 1s.
4.The anti-diagonal (top-right to bottom-left)
contains 2s.
5.Overlapping cells (center in odd-sized grids)
should have 3.
6.Print the grid in a readable matrix format'''
matrix = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        if i == j:
            matrix[i][j] = 1  # Main diagonal
        if i + j == 2:
            matrix[i][j] = 2  # Anti-diagonal
        if i == 1 and j == 1:
            matrix[i][j] = 3  # Center cell for odd-sized grid


# Print the matrix in a readable format
for row in matrix:      
    print(" ".join(str(cell) for cell in row))