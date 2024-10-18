###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
char=0
while char != len(text):
    if text[char] in vowels:
        vowel_count+=1
    char+=1
# Count vowels in the text


print(f"The number of vowels in the text is: {vowel_count}")
