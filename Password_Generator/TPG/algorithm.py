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

    vowels = 'aeiouAEIOU'
    return ''.join([char for char in answer if char not in vowels])

#add length as number to answer
def addLength(answer):
    length = len(answer)
    #answer += str(length)
    return str(length)

#add the word in reverse
def addReverse(answer):
    return answer[::-1]

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
    
    #function that will convert 2 digit numbers
    def convert_chunk(n):
        chunk_words = ''
        tens_digit = (n % 100) // 10 # 23 // 10 = 2
        ones_digit = n % 10 #3 % 10 = 3
        
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
    
    return removeSpaces(convert_chunk(number))

#--------------------------------------------------------------------------------------------------------------

#validating the password to ensure it has met all security rules
def validate_password(password):
    if len(password) < 8:
        password = addReverse(password)
    elif len(password) < 11:
        password = addLength(password)
    if not re.search("[A-Z]",password):
        password = password[0].upper() + password[1:]
    if not re.search("[0-9]",password):
        password += addLength(password)
    if not bool(re.search('[^a-zA-Z0-9]', password)):
        password = replaceVowels(password)

    return password


def choose_function(answer):
    print('--------------------------------')
    print(answer)
    print('--------------------------------')
    if 'and' in answer:
        answer = removeAnd(answer)
        
    if len(answer.split()) > 3:#if more than 3 words
        return abbreviate(answer)
    
    #whenever anything is added to the password string add an equivalent string explaining what happened
    if ' ' in answer:
        answer = removeSpaces(answer)
        
    number = random.randint(1,2)
    if len(answer) < 4:
        if number == 1:
            return answer + str(addLength(answer))
            # number = number_to_words(number)
        elif number == 2:
            return answer + str(addReverse(answers[0]))
    else:
        if number == 1:
            return replaceVowels(answer)
        elif number == 2:
            return removeVowels(answer)

def generate_password(answers):
    password = ''
    password += choose_function(answers[0][0])
    password += choose_function(answers[1][0]) + emotion(answers[1][1])
    password += number_to_words(int(answers[2][0]))


    password = validate_password(password)
    return password
 
#answers = ['violet', 'pirates of the carribean','central studio'] #either 3 answer only or 2 answers and a twoanswer
# answers = (['violet'],['arya star and two','happy'], [20])
#the array that has the answers cold be a tuple 
#the two answer question will have 2 places and there could be a third place that has a nuber specifying which function should be used for this answer

