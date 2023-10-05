'''
This code decrypts a caesar cypher without the key using brute force to get a list of 
26 possibilities. And then using a dictionary search from a list of 3000 words to find
the sentence with the most amount of valid words. 

One successful test for the code was "THISCLASSISONEOFMYFAVOURITES" which I had cyphered into 
"AOPZJSHZZPZVULVMTFMHCVBYPALZ" using the key '7'. 
'''

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isupper():
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A')) 
            #using UNICODE values to find characters before the character.
            decrypted_text += decrypted_char
    return decrypted_text

def load_english_words():
    # Simple function loads txt file of dictionary file path subject to change
    filePath = "./assignments/assignment1/dictionary.txt" 
    with open(filePath, "r") as file:
        english_words = set(word.strip().upper() for word in file)

    # Making them in descending order since we want to search long words before short words
    # As the long words might contain a shorter word in itself.
    english_words = sorted(english_words, key=lambda word: len(word), reverse=True)

    return english_words

def dictionary_lookup(decrypted_texts, english_words):
    
    valid_decryption = None
    max_word_count = 0

    # Looping through both the possible decryptions and every word in the dictionary (3000 words)
    for decrypt in decrypted_texts:
        currentIndex = 0
        count = 0
        while currentIndex < len(decrypt):
            match_found = False
            for word in english_words:
                if decrypt.startswith(word, currentIndex):
                    # If the possible decryption has a word in it
                    # move the search the next set of letters and add to count
                    currentIndex += len(word)
                    count += 1
                    match_found = True
                    break
            if not match_found:
                break  

        # The decrypt possiblity with the most number of valid words gets saved
        if count > max_word_count:
            max_word_count = count
            valid_decryption = decrypt

    return valid_decryption



def brute_force_caesar_cipher(ciphertext):
    # This loops through the ceasar cypher with 26 keys to generate every possiblity. 
    decrypted_texts = []
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        decrypted_texts.append(decrypted_text)
    return decrypted_texts


# This is the main function that brings all the subroutines together 

ciphertext = input("Enter the Caesar ciphered text (uppercase, no spaces): ")

if ciphertext.isalpha() and ciphertext.isupper():
    decrypted_list = brute_force_caesar_cipher(ciphertext)
    english_words = load_english_words()
    valid_decryption = dictionary_lookup(decrypted_list, english_words)
    print(valid_decryption)

else:
    print("Input should be all uppercase letters without spaces.")


'''
The following code was used initially to format the dictionary into uppercase and descending lenght:

filePath = "./dictionary.txt"
filePath2 = "./dictionary2.txt"
def make_uppercase(input_file_path, output_file_path):
    with open(input_file_path, "r") as file:
        lines = [line.strip().upper() for line in file]
    
    with open(output_file_path, "w") as output_file:
        for line in lines:
            output_file.write(line + '\n')

def load_and_save_english_words_sorted(input_file_path, output_file_path):
    # Make the text in the input file all uppercase
    make_uppercase(input_file_path, output_file_path)

    with open(output_file_path, "r") as file:
        english_words = [word.strip().upper() for word in file]
    
    # Sort the words from longest to shortest
    english_words_sorted = sorted(english_words, key=lambda word: len(word), reverse=True)
    
    # Write the sorted words to a new file
    with open(output_file_path, "w") as output_file:
        for word in english_words_sorted:
            output_file.write(word + '\n')
load_and_save_english_words_sorted(filePath, filePath2)
'''