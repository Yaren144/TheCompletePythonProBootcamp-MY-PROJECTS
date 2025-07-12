import string
alphabet = list(string.ascii_lowercase)



game_on = True



#encode
def encrypt(message_list,shift):

    text_e = message_list
    while shift > 25:
        shift-=25
    else:
        for i in range(len(text_e)):
            if text_e[i] not in alphabet:
                pass
            else:
                letter = text_e[i]
                new_ind = alphabet.index(letter) + shift
                if new_ind>25:
                    new_ind-=26
                elif new_ind<0:
                    new_ind +=26

                text_e[i] = alphabet[new_ind]
        print("".join(text_e))
        
    

#decode
def decrypt(message_list,shift):
    text_e = message_list
    while shift > 25:
        shift-=25
    else:
        for i in range(len(text_e)):
            if text_e[i] not in alphabet:
                pass
            else:
                letter = text_e[i]
                new_ind = alphabet.index(letter) - shift
                if new_ind>25:
                    new_ind-=26
                elif new_ind<0:
                    new_ind +=26
                text_e[i] = alphabet[new_ind]
        print("".join(text_e))






while game_on:
    code_type= input("Type encode to 'encrypt'. Type decode to 'decrypt':")
    original_text = input("Type your message: ").lower()
    shift = int(input("Type shift amount: "))
    origin_list = list(original_text)

    if code_type== "encode":
        encrypt(origin_list,shift)
        
    elif code_type== "decode":
        decrypt(origin_list,shift)

    cont  = input("Do you want to continue the game? Type: 'Yes' or 'No'")
    if cont == "Yes":
        game_on= 1
    else:
        game_on = 0
        break

    



