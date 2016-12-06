import json
import argparse

'''
	Turns a .txt file into a JSON file.
'''

def file_to_text(file_name):
	'''
		Requires a filename
		Returns a list where each element is a single word, and
		where all standalone digits have been stripped from the text (chapter
		numbers and the like)
	'''
	f = open(file_name)
	words = []

	# Read .txt file into gigantic list of words
	for word in f.read().split():
		words.append(word)

	return [x for x in words if not x.isdigit()]

def create_markov(source_text):
	'''
		Requires a source text
		Returns the markov chain dictionary/table
	'''
	markov_chain = {}

	# start with first two words in the text
	word_1 = source_text[0]
	word_2 = source_text[1]

	for i in range(len(source_text) - 1):
		try:
			word_1 = source_text[i]
			word_2 = source_text[i + 1]
			word_3 = source_text[i + 2]
		except IndexError:
			break

		word_pair = (word_1, word_2)
		word_pair = ' '.join(word_pair)

		if word_pair not in markov_chain:
			markov_chain[word_pair] = []

		markov_chain[word_pair].append(word_3)

	return markov_chain

def handle_cmd_args():
	descrip_msg = 'Produce a JSON file holding a Python dictionary representing' \
				  'markov chains built from a source text.'

	help_msg = 'Your source text/corpus for building the markov chain(s) from.'
	parser = argparse.ArgumentParser(description=descrip_msg)
	parser.add_argument('-f', '--source-file', help=help_msg, required=True)
	parser.add_argument('-o', '--output', help='Output filename for JSON file.', \
						default="markov.json")

	return parser.parse_args()

def main():
	args = handle_cmd_args()
	text = file_to_text(args.source_file)
	markov_dict = create_markov(text)

	with open(args.output, 'w') as fp:
		json.dump(markov_dict, fp, indent=4)



if __name__ == '__main__':
	main()


