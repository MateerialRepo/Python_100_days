alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_num):
  cipher_text = ""
  for char in plain_text:
    new_index = alphabet.index(char) + shift_num
    cipher_text+=alphabet[new_index]
  print(f"The encoded text is {cipher_text}")

 def decrypt(cipher_text, shift_num)):
  plain_text = ""
  for letter in cipher_text:
    index = alphabet.index(letter)
    new_index = position - shift_amount
    plain_text+= alphabet[new_index]
  print(f"The decoded test is {plain_text}")
  
if (direction == 'encode'):
  encrypt(plain_text=text, shift_num=shift)
else:
  decrypt(cipher_text=text, shift_num=shift)
