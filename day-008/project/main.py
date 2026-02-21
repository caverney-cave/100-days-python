from art import logo

alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
restart = True


def caesar(choice, original_text, shift_amount, ):
    result = ""

    if choice == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result += alphabet[new_position]
        else:
            result += letter

    print(f"Here's the {choice}d result: {result}")


while restart:

    print(logo)
    print("================================================================")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(direction, text, shift)

    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

    if user_input not in ['yes', 'y']:
        restart = False
        print("Good bye!")
