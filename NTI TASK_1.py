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

