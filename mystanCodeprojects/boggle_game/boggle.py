"""
File: boggle.py
Name: Eileen Hung
----------------------------------------
This file is a boggle game.
After the user entered 16 letters, this file will
find out all possible words(at least 4 letters) in
4*4 grid. A letter can be used only one time and
can move to another if it is adjacent.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DIRECTION = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def main():
	"""
	TODO: This program is a boggle game. The user can enter
		16 letters(4*4 square grid) and the program will
		find all possible words which are at least 4
		letters long.
	"""
	d = {}  # A Python dict to store the words(at least 4 words) in 'dictionary.txt'
	read_dictionary(d)
	# print(d) # test
	boggle = []
	enter_letters(boggle)
	print(boggle)
	if len(d) < 5:  # d doesn't collect 4 rows of letters
		return
	start = time.time()
	####################
	pass_info = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # mark 0 as not passed
	answers = []
	for x in range(4):
		for y in range(4):
			solver(boggle, x, y, pass_info, '', answers, d)
	print(f'There are {len(answers)} words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def solver(boggle, x, y, pass_info, word, ans, d):
	"""
	:param boggle: list of lists, including all letters in 4*4 letters grid
	:param x: int, index of the row of letters
	:param y: int, index of the number in row
	:param pass_info: list of lists, a 4*4 grid storing 0(not passed) and 1(passed)
	:param word: str, the word to be searched in d
	:param ans: list, stores all possible words
	:param d: dict, keys are all letters and the value to the key is a list of all
				words starting from the key letter
	:return: put all possible words in the boggle into ans
	"""
	# base case
	if len(word) >= 4 and word in d[word[0]] and word not in ans:
		print(f'Found \"{word}\"')
		ans.append(word)
	# choose
	pass_info[x][y] = 1  # 從最左上角的位置開始先往下再往右 依依選字
	word += boggle[x][y]
	# loop over neighborhood
	for direct in DIRECTION:
		if has_prefix(word, d):
			i, j = direct
			nx, ny = x + i, y + j
			if valid(nx, ny, pass_info):  # 代表是還沒通過的鄰居
				# explore
				solver(boggle, nx, ny, pass_info, word, ans, d)
	# un-choose
	pass_info[x][y] = 0


def valid(nx, ny, pass_info):
	return (0 <= nx < 4) and (0 <= ny < 4) and not (pass_info[nx][ny] == 1)


def enter_letters(boggle: list):
	for i in range(1, 5):
		row = input(f'{i} row of letters: ')
		row.lower()
		if len(row) != 7:  # Check whether users entered only 7 times(4 for letters, 3 for space)
			print('Illegal input')
			return
		row = row.split()
		if len(row) != 4:  # Check whether users entered 3 spaces to split every letters
			print('Illegal input')
			return
		boggle.append(row)


def read_dictionary(d):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dict. The
	words in this dict are all at least four words.
	"""
	with open('dictionary.txt', 'r') as f:
		for line in f:
			w = line[0:len(line)-1]
			if len(w) >= 4:
				if w[0] in d:
					d[w[0]] += [w]
				else:
					d[w[0]] = [w]


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param d: (dict) A dictionary stores all the words which are at least 4 words
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	words_lst = d[sub_s[0]]
	if sub_s in words_lst:
		return True
	for word in words_lst:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
