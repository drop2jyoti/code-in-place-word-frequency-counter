import matplotlib.pyplot as plt
import string
import numpy as np
from operator import itemgetter

# Read the file line by line and analyse the word frequency
def count_frequency(file_location):
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    try:
        with open(file_location, "r") as file:
            for line in file:
                # Remove the leading spaces and newline character
                line = line.strip()

                # Convert the characters in line to
                # lowercase to avoid case mismatch
                line = line.lower()

                # Remove the punctuation marks from the line 
                line = line.translate(line.maketrans("", "", string.punctuation)) 
                # Remove the digits marks from the line 
                line = line.translate(line.maketrans("", "", string.digits)) 
                # Split the line into words
                words = line.split(" ")
                # Iterate over each word in line
                for word in words:
                    if word == "":
                        continue
                    # Check if the word is already in dictionary
                    if word in d:
                        # Increment count of word by 1
                        d[word] = d[word] + 1
                    else:
                        # Add the word to dictionary with count 1
                        d[word] = 1

        # sort the dictionary by the frequency count values, in Descending order
        sortedDict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        return sortedDict
    except IOError:
            print("Invalid file location")
            return None

# feature to write the word and frequency into file  
def write_to_file(sortedDict, file_location):  
    # make a new text file, then write results to that
    with open(file_location, 'w') as f:
        for key in list(sortedDict.keys()):
            f.write(f"{key} ----> {sortedDict[key]}\n")  
 
 # make a new text file, then write user input to that
def create_user_input_file(lines):  
    try:
        with open("userText.txt", 'w') as f:
            for item in lines:
                f.write(item + '\n')
    except IOError:
            print("Error writing into the file from user input")

#print the word and the frequency on console
def print_the_words_with_frequency(sortedDict):
    for key in list(sortedDict.keys()):
        print(f"{key} ===> {sortedDict[key]}\n")  

# Matplot to generate a plot
def plot_graph(sortedDict):
    #Plot top 20 words
    top_20 = dict(sorted(sortedDict.items(), key=itemgetter(1), reverse=True)[:20])
    data_words = top_20.keys()
    words_counts = top_20.values()
    indexes = np.arange(len(data_words))
    width = 0.3
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.bar(indexes, words_counts, width)
    plt.xticks(indexes + width * 0.5, data_words)
    
    plt.title(label="Top 20 Word Frequency counter",
          loc="left",
          fontstyle='italic')
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()        
    plt.show()

def main():
    user_input = input("Read text from console or local file location. Choose 1 for to input through console and 2 for input through file :")
    result = None
    if user_input == "1":
        print("Enter Text. To continue entering more press enter or else press q to quit: ")
        lines = []
        while True:
            line = input()
            if  line.rstrip().lower()=='q':
                break
            else:
                lines.append(line)
        create_user_input_file(lines)
        result = count_frequency("userText.txt")
    elif user_input == "2":
        file_name = input("Enter relative path of file : ")
        result = count_frequency(file_name)
    else:
        print("Incorrect choice!")

    if result != None:
        print("\n\n######## Word Frequency Occurrence Details ########")
        print("Total number of words:" , len(result))
        print("Most common word used is: " , max(result, key=result.get))
        print("######################################################")
        print("{}   ===>   {}".format("WORDS", "COUNT"))
        print("\n")
        #print_the_words_with_frequency(result)
        print("#####################################################")
        print("########### Plotting the graph please wait.... ########")
        plot_graph(result)
        print("########### Plotting finished ########")
    else:
        print("Result is unavailable")
       
if __name__ == "__main__":
    main()
