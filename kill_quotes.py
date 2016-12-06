f = open("infinite-jest.txt")
words = []


for word in f.read().split():
	words.append(word)

string = " ".join(words)

new = string.replace(u"\u2019", "")
new = new.replace(u"\u2018", "")
new = new.replace("]", "")

with open("ij-text.txt", "w") as text_file:
    print(new, file=text_file)