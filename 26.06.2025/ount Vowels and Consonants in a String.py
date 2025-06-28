s = "Python Programming"
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in s if char in vowels)
consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
