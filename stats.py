def count_words(text) :
    words = text.split()
    return len(words)

def count_letters(text):
    letter_counts = {}
    for char in text:
        char = char.lower()
        
        if char in letter_counts :
            letter_counts[char] += 1
        else :
            letter_counts[char] = 1

    return letter_counts

def sort_character_count(char_dict) :
    new_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            new_list.append({"char":char,"num": count} )

    def sort_on(dict) :
        return dict["num"]
    new_list.sort(reverse = True, key = sort_on)
    
    return new_list




# Add a new function to your stats.py file that takes the dictionary of characters and their 
# counts and returns a sorted list of dictionaries.
#Each dictionary should have two key-value pairs: one for the character itself and one for 
# that character's count (e.g. {"char": "b", "num": 4868}).

#Sort the list from greatest to least by the count.
#The .sort() method will be helpful here (see the hint).

#Import and call the function in main.py, and capture the result.
#Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.

