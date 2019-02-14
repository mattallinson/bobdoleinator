import csv 

def filename_maker(number_of_letters, intersections):
	filename = "output" + str(number_of_letters) + "-".join(intersections) + ".tsv"
	return filename

def word_length_list_maker(number_of_letters, words):
	right_length_words = []
	for word in words:
		if len(word) == number_of_letters:
			right_length_words.append(word)

	return right_length_words

def intersecting_words(intersections, number_of_letters, words):
    check_list = []
    word_list = word_length_list_maker(number_of_letters, words)
    print(len(word_list))
    for word in word_list:
        check_list.append([word, [word[i] for i in intersections]])
    
    matches = []
    for c in check_list:
        trial = [c[0]]
        inters = c[1]
        for c in check_list:
            if c[1] == inters and c[0] not in trial:
                trial.append(c[0])
        if len(trial)>1 and sorted(trial) not in matches:
            matches.append(sorted(trial))
            print(sorted(trial))
    
    return matches

def main():
	with open('dictionary.txt', 'r') as dictionary:
	    words = [line.rstrip() for line in dictionary]
	    print(len(words), 'words in dictionary.txt')

	number_of_letters = int(input('how many letters should the word be>'))
	intersections = [int(i)-1 for i in input(
		'''which letters should match? (please enter comma separated digits)>''').split(',')]

	iw = intersecting_words(intersections, number_of_letters, words)
	
	filename = filename_maker(number_of_letters, intersections)
	with open(filename,'w', newline='') as o:
		csvwriter = csv.writer(o, delimiter='\t', lineterminator='\n')
		for i in iw:
			csvwriter.writerow(i)

if __name__ == '__main__':
	main()
