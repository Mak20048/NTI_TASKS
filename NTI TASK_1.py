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