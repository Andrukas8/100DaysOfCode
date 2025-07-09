def encode(message, shift):
    message_origin = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_encoded = ""

    for letter in message_origin:
        if letter in alphabet:
            message_encoded += alphabet[(alphabet.index(letter) + shift) % 26]
        else:
            message_encoded += letter

    return message_encoded


def decode(message, shift):
    message_encoded = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_decoded = ""

    for letter in message_encoded:
        if letter in alphabet:
            message_decoded += alphabet[(alphabet.index(letter) - shift) % 26]
        else:
            message_decoded += letter

    return message_decoded


print('''
                       _                              _           
                      | |                            | |          
  ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
| (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
            __/ | |              __/ |         | |           __/ |
           |___/|_|             |___/          |_|          |___/ 
''')


user_action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
user_message = input("Type your message:\n")
user_shift = int(input("Type the shift number:\n"))

if user_action == "encode":
    print("Here's the encoded result:")
    print(encode(user_message, user_shift))
elif user_action == "decode":
    print("Here's the decoded result:")
    print(decode(user_message, user_shift))
else:
    print("Incorrect input")
