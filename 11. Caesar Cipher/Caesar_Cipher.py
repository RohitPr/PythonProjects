from Art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w',
            'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        end_txt = ""
        if shift > 25:
            shift %= 25

        if direction == "decode":
            shift *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                end_txt += alphabet[new_position]
            else:
                end_txt += char
        print(f"\nThe {direction}d text is {end_txt}")

    caesar(text, shift, direction)

    run = input("\nDo you want to run again? Yes or No : ")
    if run == 'No':
        run = False
        print("GoodBye!")
