import string
alphabet = list(string.ascii_lowercase)

def normalize_shift(shift_amount):
    return shift_amount % 26

# encode
def encrypt(message_list, shift_amount):
    text_e = message_list

    for i in range(len(text_e)):
        if text_e[i] not in alphabet:
            pass
        else:
            letter = text_e[i]
            new_ind = normalize_shift(alphabet.index(letter) + shift_amount)
            text_e[i] = alphabet[new_ind]
    print(f"Encoded message:{"".join(text_e)}")
         

# decode
def decrypt(message_list, shift_amount):
    text_d = message_list

    for i in range(len(text_d)):
        if text_d[i] not in alphabet:
            pass
        else:
            letter = text_d[i]
            new_ind = normalize_shift(alphabet.index(letter) - shift_amount)
            text_d[i] = alphabet[new_ind]
    print(f"Decoded message:{"".join(text_d)}")

def main():
    while True:
        code_type= input("Type encode to 'encrypt'. Type decode to 'decrypt':")
        original_text = input("Type your message: ").lower()
        shift_amount = int(input("Type shift amount: "))
        origin_list = list(original_text)

        if code_type == "encode":
            encrypt(origin_list,shift_amount)
            
        elif code_type == "decode":
            decrypt(origin_list, shift_amount)

        game_on = input(
            "Do you want to continue the game? Type: 'Yes' or 'No'"
            ).lower()
        if game_on == "no":
            break


if __name__ == "__main__":
    main()
