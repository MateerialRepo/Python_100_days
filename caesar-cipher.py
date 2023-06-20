alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_num, action):
  result = ""
  if (action == 'decode'):
    shift_num *= -1
  for letter in input_text:
    if letter not in alphabet:
      result += letter
      continue
    position = alphabet.index(letter)
    new_position = position + shift_num
    result += alphabet[new_position]
  print(f"The {action}d text is {result}")
  
 if shift > 26:
  shift = shift%26
  
 caesar(input_text=text, shift_num=shift, action=direction)
