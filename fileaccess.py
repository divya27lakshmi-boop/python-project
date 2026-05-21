file = open("sample.txt", "r")

data = file.read().lower()   
file.close()


char_count = {}


vowels = "aeiou"
vowel_count = 0

for ch in data:

    
    if ch.isalpha():

        
        if ch in vowels:
            vowel_count += 1

        
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

print("Repeated Characters in Alphabetical Order:\n")

for ch in sorted(char_count):

    if char_count[ch] > 1:
        print(ch, "->", char_count[ch], "times")

print("\nTotal Number of Vowels:", vowel_count)
