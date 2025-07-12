import string
alphabet = list(string.ascii_lowercase)

def normalize_shift(shift):
    """
    Normalize shift value to bw within 0-25 range.

    Args:
        shift (int): The shift amount

    Returns:
        int:Normalised shift value
    """
    

    
    return shift % 26


def encrypt(message, shift):
    """
    Encrypt given message.

    Args:
        message (str): the message to encrypt
        shift (int): The shift amount
    """
    text_e = message

    for i in range(len(text_e)):
        if text_e[i] not in alphabet:
            pass
        else:
            letter = text_e[i]
            new_ind = normalize_shift(alphabet.index(letter) + shift)
            text_e[i] = alphabet[new_ind]
    print(f"Encoded message:{"".join(text_e)}")
         


def decrypt(message, shift):
    """
    Decrypt given message.

    Args:
        message (str): The message to process
        shift (int): shift amount
    """
    text_d = message

    for i in range(len(text_d)):
        if text_d[i] not in alphabet:
            pass
        else:
            letter = text_d[i]
            new_ind = normalize_shift(alphabet.index(letter) - shift)
            text_d[i] = alphabet[new_ind]
    print(f"Decoded message:{"".join(text_d)}")

def main():
    """
    Main function to run the Ceasar cipher program.
    """
    while True:
        code_type= input("Type encode to 'encrypt'. Type decode to 'decrypt':")
        original_text = input("Type your message: ").lower()
        shift = int(input("Type shift amount: "))
        origin_list = list(original_text)

        if code_type == "encode":
            encrypt(origin_list,shift)
            
        elif code_type == "decode":
            decrypt(origin_list, shift)

        game_on = input(
            "Do you want to continue the game? Type: 'Yes' or 'No'"
            ).lower()
        if game_on == "no":
            break


if __name__ == "__main__":
    main()
