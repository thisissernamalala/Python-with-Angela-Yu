import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

my_pass = ""

passs = []
for letts in range(1,nr_letters+1):
    lett = random.choice(letters)
    passs.append(lett)
for sybs in range(1,nr_symbols+1):
    syb = random.choice(symbols)
    passs.append(syb)
for nums in range(1, nr_numbers+1):
    num = random.choice(numbers)
    passs.append(num)

random.shuffle(passs)
password = ""
for i in passs:
    password+=i
print(f"Your new Password is: {password}")