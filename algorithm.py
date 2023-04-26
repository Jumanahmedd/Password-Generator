import re
import random 

#replaces all the vowels with number or symbols
def replaceVowels(answer):

    vowels_dict = {'a':'@','e':'9','i':'!','o':'0','u':'()'}
    counter = len(answer)
    for i in answer:
        if i in vowels_dict:
            answer = answer.replace(i,vowels_dict[i])
            if (counter+2) == len(answer):
                break
    return answer

#removes all vowels  except first and last letters
def removeVowels(answer):

    vowels = ['a','e','i','o','u']
    for i in range(1,len(answer)):
        if answer[i] in vowels:
            answer = answer.replace(vowels,'')

#add length as number to answer
def addLength(answer):
    length = len(answer)
    #answer += str(length)
    return length

#add the word in reverse
def addReverse(answer):
    return answer[::-1]


#def eachWordLength(answer):

#remove white spaces and capitalize letters to show the words
def removeSpaces(answer):
    answer = " ".join(word.capitalize() for word in answer.split())
    answer = answer.replace(' ','')
    return answer

#get the abbreviations of large sentences
def abbreviate(answer):
    abbrev = answer[0]
    for i in range(1, len(answer)):
        if answer[i-1] == ' ':
            abbrev += answer[i]
    
    abbrev = abbrev.upper()

    return abbrev

def removeAnd(answer):
    if 'and' in answer:
        answer = answer.replace('and','&')
        return answer


#use symbols to create emojis 
def emotion(answer):
    switcher = {
        "happy": ":)",
        "sad":":(",
        "confused":";}",
        "excited":":D",
        "emotional":";<",
        "speechless": ":!" 
    }
    return switcher.get(answer,"")


#Converts a number to its string representation.
def number_to_words(number):

    # Define dictionaries for number names
    ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    thousands = {0: '', 1: 'thousand', 2: 'million', 3: 'billion'}
    
    #function that will convert 2 digit numbers
    def convert_chunk(n):#123
        chunk_words = ''
        hundreds_digit = n // 100 #any 2 digit number will return a zero
        tens_digit = (n % 100) // 10 # 23 // 10 = 2
        ones_digit = n % 10 #123 % 10 = 3
        
        if hundreds_digit > 0:
            chunk_words += ones[hundreds_digit] + ' hundred '#one hundred
        
        if tens_digit == 1:
            chunk_words += teens[n % 100]
        elif tens_digit > 1:
            chunk_words += tens[tens_digit] + ' '#one hundred twenty
        
        if tens_digit != 1 and ones_digit > 0:
            chunk_words += ones[ones_digit] + ' '
        
        return chunk_words
    
    #if the number is 0
    if number == 0:
        return ones[0]
    
    # Break number into three-digit chunks and convert each chunk to words
    chunks = []
    while number > 0:#12,100
        chunks.append(number % 1000)
        number //= 1000
    
    # Convert each chunk to words then concatenate 
    words = ''
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue # to skip the next statment and return to the loop
        chunk_words = convert_chunk(chunk)
        if i > 0:
            chunk_words += ' '+ thousands[i]
        if words:
            words = chunk_words + ' ' + words
        else:
            words = chunk_words
    
    return words


#validating the password to ensure it has met all security rules
def validate_password(password):
    if len(password) > 10:
        return 1#might ask the user for another answer to add to the password
        #or we can create a function that gets the length of each answer by using the separation hyphen
        # if the pasword is missing alot od charater we can add the number in letters if not we can add it as number
    if not re.search("[A-Z]",password):
        return 2#can just capitalize the first letter
    if not re.search("[a-z]",password):
        return 3#there is no way kda we have to entirly recreate the password
    if not re.search("[0-9]",password):
        password = addLength(password)
        #validate_password(password)
    if not re.search("[!@#$%^&*()_+-=[]{};':\"\\|,.<>/?]",password):
         return 5

 
#answers = ['violet', 'pirates of the carribean','central studio'] #either 3 answer only or 2 answers and a twoanswer
answers = (['arya star and two','Sability'],['violet'], ['frank ocean','lost'])
#the array that has the answers cold be a tuple 
#the two answer question will have 2 places and there could be a third place that has a nuber specifying which function should be used for this answer
password = ''

#to choose the function that will be used with each answer 
for answer in answers:
    i = -1
    for x in answer:
        i += 1 #index number for answer
        if 'and' in x:
            x = removeAnd(x)
            answer[i] = x
        
        if len(x.split()) > 3:#if more than 3 words
            answer.remove(x)
            x = abbreviate(x)
            password += x   
            # print(answers)
            print(password)
            #whenever anything is added to the password string add an equivalent string explaining what happened
        elif ' ' in x:
            answer[i] = removeSpaces(x)
            #print(answer)

print(answers)



# if len(answers[0][0]) > 4:
#     random = random.randint(1,2)
#     if random == 1:
#         number = addLength(answers[0][0])
#         number = number_to_words(number)
#         answers[0][0] += number
#     elif random == 2:
#         answers[0][0] += addReverse(answers[0])
    
    




#make sure that no process is repeated twice for the same password
#gather all the answers after process then concatenate them using the separation symbol that will be chosen

#print(number_to_words(1210000))

# for answer in answers:
#     password = password + "_" + replaceVowels(answer)

# print(password)
#print(abbreviate(answers[1]))


#some rules for the password:
#the pasword must have all characters 
#password must be atleast 10 characters long




#I can have a one word answer eg. yellow, painting
##the last answer will be from the 2 part question that will include an answer and an emotion or 
#then the number question but I need to edit the function to only tuen one of the character into letters if all where turned its too much
