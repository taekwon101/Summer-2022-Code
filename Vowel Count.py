
#trial 1
word = str(input('print a word in lowercase letters: '))
vowel = ["a", "e", "i", "o", "u"]

for vowel in word:
        if vowel == "a":
            first = +1
        elif vowel in word:
            if vowel =="e":
               second = +1
        elif vowel in word:
             if vowel == "i":
                 third = +1
        elif vowel in word:
               fourth = +1
        else:
            if vowel == "u":
                fifth = +1 

total = first + second + third + fourth + fifth 

print(total)

input()






#trial 2
def vowel_count(str):
	
vowel = set("aeiou")
	for alphabet in str:
		if alphabet in vowel:
 			count = count + 1
	
print("Number of vowels :", count)




#trial 3
word = input("print word in lowercase letters: ")
print(word)

for vowel in word:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        total = +1 

print(total)
        
input()



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