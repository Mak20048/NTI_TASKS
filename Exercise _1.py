#Exercise 01
#Write a Python program that does the following:
#Asks the user to enter their name. 
# #Asks the user to enter the prices of 3 products in one line, separated by spaces.
# Calculates the total price of the three products.Applies a 10% discount to the total.#
# Prints this message: ‘hey name the price after the discount is 90% of the total price, which is total_price_after_discount’.
name=input("Enter your name:  ")
print("Hello, welcome to our store!")
prices = list(map(float,input("Enter three prices to the three products  :  ").split()))
sum_prices = sum(prices)
print (f'hey {name}, the total price of the three products is {sum_prices}  ')
print (f'Hey {name}, the price after the discount is 90 percent of the total price, which is {sum_prices*0.9}  ')
