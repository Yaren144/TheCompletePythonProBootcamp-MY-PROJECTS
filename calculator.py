def calculator(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return  subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        print("Enter a valid operation.")

    
def input_taker(keep_num="n",num1=None):

    if keep_num == "y":
        first_num = num1
    elif keep_num == "n":
        first_num = int(input("What is the first number?: "))


    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_num = int(input("What is the next number?: "))
    result = calculator(first_num, second_num, operation)

    if result is not None:
        print(f"{first_num} {operation} {second_num} = {result}")

    return result


def keep_number():
    keep_num = input().lower()
    return keep_num

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
 
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None



def main():
    game_on = True
    keep_letter = ["y","n"]
    keep_num = "n"
    result_n = None

    while game_on:

        if keep_num =="exit":
            game_on = False
            break

        if keep_num not in keep_letter:
            print("Enter a valid letter.")
            break
        else:
            if keep_num == "y" and result_n is not None:
                result = input_taker("y",result_n)
            else:
                result = input_taker()

            result_n = result

            if result is not None:
                print(f"If you want to continue with {result_n} enter 'y' or with a new number 'n' (EXIT is 'exit')")
                keep_num = keep_number()
            
            else:
                print("Error in calculation. Starting over...")
                keep_num = "n"


            

            
            
                
                



if __name__ == "__main__":
    main()