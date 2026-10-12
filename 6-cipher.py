alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    result = ""
    for char in text.lower():
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char 
    return result

def decrypt(text, shift):
    result = ""
    for char in text.lower():
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char 
    return result

answer = 'yes'

def start():
    global answer
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    message = input("Type your message: \n").lower()
    shift = int(input("Type shift number: \n"))

    if direction == 'encode':
      print(f"Here's the encoded: {encrypt(message, shift)}")
    else:
      print(f"Here's the decoded: {decrypt(message, shift)}")

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

start()

while answer == 'yes':
  start()