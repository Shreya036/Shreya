file=open("sample.txt","r")
text=file.read()
file.close()
paragraph=len(text.split("\n"))
vowels=0
consonants=0
for i in text:
    if i.lower() in "aeiou":
        vowels+=1
    elif i.isalpha():
        consonants+=1
print("paragraph=",paragraph)
print("vowels=",vowels)
print("consonants=",consonants)
