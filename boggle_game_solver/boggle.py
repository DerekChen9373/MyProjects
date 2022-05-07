FILE = 'dictionary.txt'
all_words = {}

def main():

	while True:
		read_dictionary()
		l_1 = input('1 row of letters: ').split(' ')
		l_2 = input('2 row of letters: ').split(' ')
		l_3 = input('3 row of letters: ').split(' ')
		l_4 = input('4 row of letters: ').split(' ')
		count=0
		for lst in [l_1, l_2, l_3, l_4] :
			for elememt in lst:
				if len(elememt) != 1 and elememt.isalpha() == False:
					if count==0:
						print('illegal input')
					count+=1
					break
		if count != 0:
			break
		all=find_all_words([l_1, l_2, l_3, l_4])
		l=[]
		for word in all:
			if has_prefix(word[0:2]) and word in all_words[word[0:2]]:
				print(f'found: {word}')
				l.append(word)
		print(f'There are {len(l)} word(s) in total.')
		break

def find_all_words(lst):

	a = []
	all = []
	for i in range(4):
		for j in range(4):
			a.append(find_all_words_helper(lst, [], [],'', i, j))
	for lst in a:
		for element in lst:
			all.append(element)
	return all

def find_all_words_helper(lst, all ,walked ,word, x1, y1):

	if word.lower() not in all and len(word) >= 4:
		all.append(word.lower())
	if (x1, y1) in walked or x1 in (4, -1) or y1 in (4, -1) or len(word)>=6:
		pass
	else:
		word += lst[y1][x1]
		walked.append((x1, y1))
		for x, y in [(1,0), (0,1), (1,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1)]:
			find_all_words_helper(lst, all, walked, word, x1 + x, y1 + y)
		word = word[0:len(word) - 1]
		walked.pop()
	return all

def read_dictionary():

	with open(FILE, 'r') as f:
		for line in f:
			global all_words
			if line[0:2] in all_words:
				all_words[line[0:2]].append(line[0:len(line) - 1])
			else:
				all_words[line[0:2]] = []
				all_words[line[0:2]].append(line[0:len(line) - 1])

def has_prefix(sub_s):

	if sub_s in all_words:
		return True
	else:
		return False

if __name__ == '__main__':
	main()
