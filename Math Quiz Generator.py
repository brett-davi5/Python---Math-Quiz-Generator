
# coding: utf-8

# In[3]:

from random import randint
import random

def greeting():
    print("Welcome to the Random Math Quiz!")
    print("We'll be creating a randomly generated series of math questions for you. Let's get started!")
    
def numberOfQuestions():
    while True:
        try:
            number = int(input("How many questions would you like to generate? (1-100)"))
            if(number < 1 or number > 100):
                print("I'm sorry but your number is out of range. Please select a number between 1 and 100.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please select a number between 1 and 100.")

def numberOfDigits():
    while True:
        try:
            number = int(input("How many digits would you like each number to be? (1-4)"))
            if(number < 1 or number > 4):
                print("I'm sorry but your number is out of range. Please select a number between 1 and 4.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please select a number between 1 and 4.")

def addition():
    choice = input("Would you like to include addition (+) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("+")
    else:
        print("Please select either Y or N for your answer.")
        addition()

def subtraction():
    choice = input("Would you like to include subtraction (-) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("-")
    else:
        print("Please select either Y or N for your answer.")
        subtraction()

def division():
    choice = input("Would you like to include division (/) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("/")
    else:
        print("Please select either Y or N for your answer.")
        division()

def multiplication():
    choice = input("Would you like to include multiplication (*) operations? [Y/N]")
    if choice == "Y" or choice == "N" or choice == "y" or choice == "n":
        if choice == "Y" or choice == "y":
            operators.append("*")
    else:
        print("Please select either Y or N for your answer.")
        multiplication()

def createDigit():
    numberOfDigits = digits
    if(numberOfDigits == 1):
        return random.randint(1,9)
    if(numberOfDigits == 2):
        return random.randint(10,99)
    if(numberOfDigits == 3):
        return random.randint(100,999)
    if(numberOfDigits == 4):
        return random.randint(1000,9999)
        
def generateQuestions():
    questionNumbers = numberOfQuestions
    gen_problems = open(r'C:\Users\Family\Desktop\gen_problems.txt', 'w')
    gen_problems_answers = open(r'C:\Users\Family\Desktop\gen_problems_answers.txt', 'w')
    while questionNumbers > 0:
        digit1 = createDigit()
        digit2 = createDigit()
        operator = random.choice(operators)
        
        question = (str(digit1) + operator + str(digit2))
        
        if(operator == "+"):
            questionAnswers = digit1 + digit2
        if(operator == "-"):
            questionAnswers = digit1 - digit2
        if(operator == "*"):
            questionAnswers = digit1 * digit2
        if(operator == "/"):
            valueCheck = digit1 / digit2
            fullIntegerCheck = valueCheck % 10
            if(fullIntegerCheck == 0):
                questionAnswers = valueCheck
            else:
                questionAnswers = int(valueCheck)
        
        gen_problems.write(str(questionNumbers)+ ".  " + question + " = ____" + "\n")
        gen_problems_answers.write(str(questionNumbers)+ ".  " + question + " = " + str(questionAnswers) +"\n")
        questionNumbers = questionNumbers - 1

def instructions():
    addition()
    subtraction()
    division()
    multiplication()
        
def mathQuiz():
    global digits
    global numberOfQuestions
    global operators
    operators = []
    
    print("Answer each of the following questions to determine the layout and setup of your math quiz.")
    numberOfQuestions = numberOfQuestions()
    digits = numberOfDigits()
    
    instructions()
    print("GENERATING QUESTIONS")
    generateQuestions()
    print("QUESTIONS COMPLETE")
    #generateAnswers()
    print("ANSWER KEY GENERATED")


# In[4]:

mathQuiz()


# In[ ]:



