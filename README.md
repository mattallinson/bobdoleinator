`bobdole.py` is a script that can go through a given text file of words and return sets of words that are the same length that have the same matching characters. For example a querey of _8 letter words that have the same 1st and 5th letter with the last letter being "m"_ would return  `["Escapism", "Europium"]`among many, many other combinations. 

#Usage:

##Windows:
1. Run `bobdole.exe`

##Linux/Mac
1. Open terminal window at folder and run `python bobdole.py`

2. Enter the number of letters you want when prompted (i.e. for the above example enter >8)
3. Fix any letters you want (i.e. for the above example enter >8:m)
4. Enter the number of the letters you want to "intersect" separated by commas (i.e. for the above example entr >1,5)

5. ????
6. When it finishes, look back in the folder you just ran the program from, you should have a file called "output_8_1-5.tsv". Open this in excel or whatever editor you wish.

*Note*
There is no error handling built in to this, so if you ask for the 9th letter of 6 letter words, it will crash. If you separate your desired number of intersections with anything other than commas, it will crash. If you enter anything that isn't a numeric number, it will crash. It will probably also crash for many other mysterious reasons. Let me know them.

#Changing the dictionary
This program opens up a file called `dictionary.txt` in it's home directory. This means you can change the words it runs from by changing this file. The rules for this file are that it has to have one word per line. Otherwise go wild. 