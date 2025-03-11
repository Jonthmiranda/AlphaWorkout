import unicodedata
import re
import random
from datetime import date

#variables
brDate = (date.today()).strftime('%d/%m/%Y') #see the date of today, and transform to BR standart
randWord = []
exercicesList = ['A - 30 High Knees', 'B - 20 Push-ups', 'C - 20 Bicycles', 'D - 1-Min Wall-sit', 'E - 15 Burpees', 'F - 30 Crunches', 'G - 30 Mountain Climbers', 'H - 30 Squats', 'I - 1 Min Jumping Jacks', 'J - 20 Tricep Dips', 'K - 1 Min Wall-sit', 'L - 30 Sec', 'M - 15 Burpees', 'N - 30 Crunches', 'O - 30 Mountain Climbers', 'P - 20 Push-ups', 'Q - 20 Bicycles', 'R - 30 High Knees', 'S - 20 Tricep Dips', 'T - 30 Mountain Climbers', 'U - 30 High Knees', 'V - 1 Min Jumping Jacks', 'W - 1 Min Wall-sit', 'X - 30 Sec Pip-ups', 'Y - 30 Crunches', 'Z - 30 Squats']
alfabet = 'abcdefghijklmnopqrstuvwxyz'
text = """Dan is the former Vice-President of the Magic Kingdom, Walt Disney World, Florida.
He attended Boston University, graduating in 1991, where he earned a Bachelor of Arts degree in Political Science. After spending 5 years working for Walt Disney in France, Dan relocated to Florida and held a variety of executive roles at the Walt Disney World Resort, both in the theme parks and resort hotels. His last 9 years with the company, he was successively Vice President of Epcot, Vice president of Disney’s Hollywood Studios and eventually Vice President of the Magic Kingdom where he led 12,000 cast members and entertained over 20 million guests annually.
After a fulfilling and exciting 26-year career with the Walt Disney Company, Dan and his wife Valerie made the decision to set out on a new venture and start their own consulting and speaking business. Dan provides customized, authentic presentations, insightful workshops, and one on one coaching, focusing on leadership and management practices drawing upon his extensive Disney career with relevant examples and inspiring storytelling.
In this episode, Jared and Dan talk about Dan's book How's the Culture in Your Kingdom? The speak about the importance of leading yourself first before you can lead others. Self-awareness is not as easy to come by as you may think. We must be intentional to grow and develop our own abilities to move into a space where we can successfully lead others.
"I may not be good at the beginning, and I may fail, but by practicing and trying, it's going to make me better, it's going to make me understand it more." - Dan Cockerell"""

def tratament(text): 
    text = text.lower() #all letters is lowercase
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('ascii') #if have any accent in letter, remove
    text = re.sub(r'[^a-zA-Z ]', '', text) #remove all special caracteres
    text = text.split() #transform text in list
    for i in text: #remove all word that have 2 caracteres or less
        leng = len(i)
        if leng < 3:
            text.remove(i)
    return text

def randomWord(text):
    text = random.choice(text) #choice a random word of the list of words
    print(f"The word of the {brDate} is '{text}'\n")
    for i in text: #make a new list with the letters of the word
        randWord.append(i)
    return text

def exercices_Save(word):
    for i in word:
        position = 0
        position = alfabet.find(i) #find the position of the letters in the alfabet
        print(exercicesList[position]) #print the exercicios of thhe word

#main
text = tratament(text)
word = randomWord(text)
exercices_Save(word)


