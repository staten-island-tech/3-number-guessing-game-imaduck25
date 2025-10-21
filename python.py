""" count = 1
while count <= 5:
    print("This is loop number", count)
    count = count + 1

order = ""
while order != "done":
    order = input("What would you like to order? (type 'done' to finish): ")
print("Thanks for your order!") """

number_game = 0
import random
x = random.randint(1, 10)
while number_game != x:
    number_game = int(input("guess the number i am thinking of. "))
print("correct")