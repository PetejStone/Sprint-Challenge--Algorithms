'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

## Set a scenario for each case value or non existent value
count = 0
i = 0
def count_th(word):
    split = word
    def recur_word(split, count=0, i=0):
        base = len(split) - 1
        if i < base:
            compare = f'{split[i]}{split[i+1]}'
            if 'th' in compare:
                count += 1
                # print(i)
                i += 1
                recur_word(split, count, i)

            i += 1
            # print(i)
            return recur_word(split, count, i)
        else:
            return count
        return count
                
    print(count)
    return recur_word(split)
        
  

# def count_th(word):
#     count = 0 # set base case to 0
#     if "th" in word: # if th is found in the word
#         print(f'"th" appears: {word.count("th")}') #printing the word
#         count = word.count("th") # set count = to the number of times th appears
#         return count #return new count
#     elif "Th" in word: # Same as above but checking for Th
#         print(f'"Th" appears: {word.count("Th")}')
#         count = word.count("Th")
#         return count
#     elif "tH" in word: #same as above but checking for tH
#         print(f'"tH" appears: {word.count("tH")}')
#         count = word.count("tH")
#         return count
#     elif "TH" in word: #same as above but checking for TH
#         print(f'"TH" appears: {word.count("TH")}')
#         count = word.count("TH")
#         return count
#     else: #If none of the above is found, they do not exist, so return the base case of zero
#         return count

 

