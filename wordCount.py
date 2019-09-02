import sys
input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

f_in = open(input_file, "r")

# All the words in a list.
words = f_in.read().replace('-',' ').replace('\'',' ').split()
dictionary = dict()

#Traverse words, clean them up, and store in dictionary
for word in words:
    clean_word = word.strip('",.!?;: ').lower()
    dictionary[clean_word] = dictionary.get(clean_word, 0) + 1
f_in.close()
    
f = open(output_file, "w+")
for i in sorted (dictionary):
    string_to_write = str(i) + " " + str(dictionary[i]) + "\n"
    f.write(string_to_write)
f.close()
