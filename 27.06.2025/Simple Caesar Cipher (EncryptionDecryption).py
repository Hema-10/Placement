def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

print(caesar_encrypt("Hello World", 3))  # Khoor Zruog
