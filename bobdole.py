import csv 

def intersecting_words(intersections, number_of_letters, words):
    check_list = []
    for word in words: 
        check_list.append([word, [word[i] for i in intersections]]) # so "spam" with intersections [1,3,4] would be >> ["spam", ["s","a","m"]]
    
    matches = []
    checked = []
    for c in check_list: #["spam", ["s","a","m"]
        trial = [c[0]] #"spam"
        inters = c[1] #["s","a", "m"]
        if inters in checked:
        	continue
        else:
        	checked.append(inters)
        
        for c in check_list: #["slam", ["s","a","m"]
            if c[1] == inters and c[0] not in trial: #True
                trial.append(c[0]) #trial = ["spam", "slam"]
        if len(trial)>1 and sorted(trial) not in matches: 
        #This loop prevents ["spam", "slam"] and ["slam", "spam"] both being added to the "matches" list
        #This is highly simple but exceedingly inefficient and should probably be replaced
            matches.append(sorted(trial))
            print(sorted(trial)) #bit of output so we've got something to watch as it does its thing
    
    return matches

def main():
	with open('dictionary.txt', 'r') as dictionary_file: #get the words
	    dictionary = [line.rstrip() for line in dictionary_file]
	    print(len(dictionary), 'words in dictionary.txt') #output to test it's worked

	#request number of letters from user
	number_of_letters = int(input('how many letters should the word be> ').rstrip())
	
	#get set letters from user
	required_letters_input = input('which letters are fixed? Enter in the format "position=letter" and leave black if none> ').rstrip()
	
	if required_letters_input == '':
		required_letters = None
	else:
		required_letters = {int(position)-1:letter for position, letter in [pair.split('=') for pair in required_letters_input.split(',')]}

	#request desired intersections from user
	intersections = [int(i)-1 for i in input('which other letters should match? (please enter comma separated digits)> ').split(',')] 
		
	

	right_length_words = [word for word in dictionary if len(word) == number_of_letters] #selects words from the dictionary that are the right length
	
	if required_letters is not None:
		#selects only letters that have the required letters at the desired positions
		words_to_test = [word for word in right_length_words if all(word[i] == required_letters[i] for i in required_letters)]
	else:
		words_to_test = right_length_words

	filename = "output_" + str(number_of_letters) + '_' + "-".join([str(i+1) for i in intersections]) +'_' + required_letters_input + ".tsv"
	#the main event: get the matches list for the users inputs
	iw = intersecting_words(intersections, number_of_letters, words_to_test) 
	
	
	with open(filename,'w', newline='') as o: #saves the file
		csvwriter = csv.writer(o, delimiter='\t', lineterminator='\n')
		for i in iw:
			csvwriter.writerow(i)

if __name__ == '__main__':
	main()
