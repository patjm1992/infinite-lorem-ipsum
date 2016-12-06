import random
import json
import argparse
import timeit

'''
	Uses a JSON file to generate text.
'''

def generate_text(markov_chain, desired_len):
	'''
		Requires the markov chain dictionary/table
		Returns a string of new text
	'''
	key = random.sample(list(markov_chain), 1)
	word_1, word_2 = ("".join(key[0])).split()

	new_passage = ''

	for i in range(desired_len):
		try:
			new_word = random.choice(markov_chain[" ".join(key)])
		except KeyError:
			print("Key not found: " + word_1, word_2)
			break

		new_passage += new_word + ' '
		word_1 = word_2
		word_2 = new_word
		combo = word_1 + ' ' + word_2
		key = combo.split()

	return new_passage

def ends_with_punctuation(w):
	'''
		Return True if word ends in a period, a question mark, or an exclamation
		False otherwise
	'''
	punct = ['.', '?', '!']

	return w[-1:] in punct

def has_quote(w):
	'''
		Return True if a word has a quote as the first or last character
		False otherwise
	'''

	return w[-1:] is "'" or w[:1] is "'"

def add_capitalization(passage):
	'''
		Requires a string of text
		Returns a string of text that is (mostly) properly capitalized
	'''

	word_list = passage.split()

	for i, word in enumerate(word_list):
		if ends_with_punctuation(word):
			try:
				word_list[i + 1] = word_list[i + 1].capitalize()
			except IndexError:
				break

	# Capitalize the first letter in the newly generated text
	word_list[0] = word_list[0].capitalize()

	capitalized = " ".join(word_list)

	return capitalized

def strip_quotes(passage):
	'''
		Requires a string of text
		Returns a string where instances like 'hello or hello' are removed
	'''
	word_list = passage.split()

	for i, word in enumerate(word_list):
		if has_quote(word_list[i]):
			word_list.remove(word)
			a = list(word)
			a.remove("'")
			word_list[i] = "".join(a)

	without_quotes = " ".join(word_list)

	return without_quotes

def trim_by_chars(passage, num_chars):
	'''
		Requires a string of text
		Returns a string of specified length
	'''


	num_chars = num_chars - 3

	if passage[(num_chars - 1):num_chars] == ' ':
		passage = passage[:num_chars]
		passage += '...'
	elif passage[(num_chars - 1):num_chars] == '.':
		passage = passage[:num_chars]
	else:
		passage = passage[:num_chars]
		passage += '-'

	return passage

def add_ending_punctuation(passage):

	sentence_ender = ['.', '...', '!', '?']

	word_list = passage.split()

	if ends_with_punctuation(word_list[len(word_list) - 1]):
		if ',' in word_list[len(word_list) - 1]:
			word_list[len(word_list) - 1] = word_list[len(word_list) - 1][:-1]
			return " ".join(word_list)
		else:
			return passage
	else:
		return passage + random.choice(sentence_ender)

def format(text):
	'''
	 	Wrapper function
	'''
	return add_ending_punctuation(strip_quotes(add_capitalization(text)))

def main(word_ct):

	with open('json/infinite-jest.json') as fp:
		markov_chain = json.load(fp)

	return format(generate_text(markov_chain, word_ct))



if __name__ == '__main__':
	main()

