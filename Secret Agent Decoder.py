alphabet = "abcdefghijklmnopqrstuvwxyz"
secret_message = "hello hamza ali mazari"
shift = 3  

scrambled_message = ""


for character in secret_message:
    if character in alphabet:
        
        old_position = alphabet.index(character)
        
        
        new_position = (old_position + shift) % 26
        
        
        new_letter = alphabet[new_position]
        
        
        scrambled_message = scrambled_message + new_letter
    else:
        
        scrambled_message = scrambled_message + character

print("Original message :", secret_message)
print("Scrambled message:", scrambled_message)
