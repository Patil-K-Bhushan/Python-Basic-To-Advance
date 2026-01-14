sentence = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sentence = sentence.lower()

for char in sentence:
    if char in vowels:
        sum += 1

print(sum)