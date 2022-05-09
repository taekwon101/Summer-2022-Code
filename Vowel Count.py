
#trial 1
word = str(input('print a word in lowercase letters: ')) #str probably not needed
vowel = ["a", "e", "i", "o", "u"] # I think I see where you were planning to take this and I like it a lot, even if it didn't get implemented here

for vowel in word: # “for [this] in [that]:” makes “[this]” into the first/second/third/etc. item in the [that] list every time it goes through the loop. I’m  surprised that having “vowel” already assigned to a different list is allowed
        if vowel == "a": # slight caution that unnecessarily double indenting might accidentally break something or be confusing in some contexts
            first = +1 # You probably mean to use the “+= 1” --- gotta initialize the variable (Python can assume a lot but it doesn't know a number starts at 0 unless you tell it)
        elif vowel in word: # "elif" means "else if" so there's already an in built in.  And you should read "if vowel in word" as "if vowel *is* in word" meaning that the condition that you're asking for here is if the letter it took from the word is in the word (which obvs it is), then execute what follows
            if vowel =="e":
               second = +1 # having separate variables isn't code-breaking, but just using "total" for all of these would have been a tad more efficient/intuitive
        elif vowel in word:
             if vowel == "i":
                 third = +1
        elif vowel in word: # skipped 'o'
               fourth = +1
        else: # used else and then if instead of elif
            if vowel == "u":
                fifth = +1 

total = first + second + third + fourth + fifth

print(total)

input()






#trial 2
def vowel_count(str): # 'def' is used to make a function which takes some kind of input, does something to it, and gives an output (makes it easy to do something repetitive without re-writing code).  Also, code will become quite painful to debug if you use things like data types (e.g., 'str') as variable names
	
vowel = set("aeiou") # I think "set()" is typically used to remove repeated elements in a list (like set(1, 1, 2, 3, 3) --> 1, 2, 3)
	for alphabet in str: # indent indicates it is a part of the code above it
		if alphabet in vowel:
 			count = count + 1
	
print("Number of vowels :", count)
# I think this should work in principle! (aside from not saying "count = 0" in the beginning and even though "set" and "def" seem strange)



#trial 3
word = input("print word in lowercase letters: ")
print(word)

for vowel in word:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        total = +1 

print(total)
        
input()
# This is great (aside from not saying "total = 0" or using "+=")


#trial 4
word = input("print word in lowercase letters: ")
print(word)

for vowel in word:
    if vowel == "a":
        total = +1
    elif vowel in word:
        if vowel =="e":
            total = +1
    elif vowel in word:
        if vowel == "i":
            total = +1
    elif vowel in word:
        if vowel == "o":    
            total = +1
    else:
        if vowel == "u":
            total = +1
grand_total = sum(total)

print(grand_total)

input()


#trial 5
word = input("print word in lowercase letters: ")
print(word)

def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiou":
           num_vowels = num_vowels+1
    return num_vowels
