#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass_let = random.sample(letters,k = nr_letters)
pass_smb = random.sample(symbols,k = nr_symbols)
pass_num = random.sample(numbers, k = nr_numbers)

password = pass_let + pass_smb + pass_num

password_easy = "".join(password)
print(f"Easy password: {password_easy}")

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)
password_hard = "".join(password)
print(f"Hard password: {password_hard}")