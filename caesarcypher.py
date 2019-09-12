sen=input("Type in the sentence you want to cypher!: ")
uni=[]
for letter in sen:
    uni.append(chr((ord(letter))+3))
print("".join(uni))

