
with open ("sample_texts/infinite-jest.txt", "r") as myfile:
    data = myfile.read()

li = list(data)

unwanted = ["(", ")", "[", "]", u"\u2018", u"\u2019", u"\u201c", u"\u201d"]

for c in unwanted:
	new_li = [x for x in li if x != c]


for c in new_li:
	for x in unwanted:
		if x == c:
			print("Found something.")

