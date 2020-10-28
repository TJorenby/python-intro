# print("Hello World")


# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# // create a variable

# character_name = "Tyler"
# character_age = "35"
# print("My name is " + character_name + ", and")
# print("I'm " + character_age + " years old")

# character_name = "Jim"
# character_age = "55"
# print("I like the name " + character_name + ",")
# print("and someday, I will be " + character_age + " years old.")

# // Basic Calculator

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# # float() for decimals. int() for integers

# print(result)

# // Madlib Game

# color = input("Enter A Color: ")
# plural_noun = input("Enter A Plural Noun: ")
# celebrity = input("Enter A Celebrity: ")

# print("roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# Functions

# from Question import Question


# def say_hi():
#     print("Hello Tyler")


# Call the function
# say_hi()

# Order of execution
# print("top")
# say_hi()
# print("bottom")

# Parameters

# def say_hello(name):
#     print("Hello " + name)


# say_hello("Tyler")
# say_hello("Jim")

# Return Statement - "code stops at 'return', just like JS"

# ////
# def cube(num):
#     return num*num*num


# result = cube(4)
# print(result)
# ////

# If Statement

# ///
# is_male = True
# is_tall = True

# if is_male and is_tall:
#     # executed when 'If' statement is true
#     print("You are a male or tall or both")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male and are not tall")
# ///

# While Loop

# ///
# i = 1
# while i <= 10:
#     print(i)
#     i += 1  # adds 1 to i

# print("done with loop")
# ///

# Multiple Choice Quiz


# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),

# ]


# def run_test(questions):
#     score = 0
#     for question in questions:  # for each question object inside of questions array, do something
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#         print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# run_test(questions)




