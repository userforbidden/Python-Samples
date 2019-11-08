"""
Mark is fan of logic based games. However he is bored of the basic ones, like Sudoku and Mastermind, since he has solved so many of them. Recently he found a new game in which one is given a string with some question marks in it. The objective is to replace all of the question marks with letters(one letter per question mark) in such a way that no letters appears next to another letter of the same kind.

Write a function:

def replaceQuestionMark(puzzle):
	pass
	''' Your code goes here '''
that given a string puzzle, returns a copy of the string with all the question marks replaced by lowercase letters(a-z) in such a way that the same letters do not occur next to each other. The result can be any of the possible answers as long as it fulfils the above requirements.

Examples:

Given puzzle = 'xy?xz?', your function might return 'xycxza'. Some other possible results are 'xyzxzd', 'xyfxzf'.

Given puzzle = 'ab?e?mr??'. Your function might return 'abveamrab'

Given puzzle = '??????'. Your function might return 'league'

Write an efficient algorithm for the following assumptions:

String puzzle contains only of lowercase letters(a-z) or '?'
It is always possible to turn string 'puzzle' into a string without two identical consecutive letters
"""
import string 
import random 
import re 

def replaceQuestionMark(puzzle):
    # find question marks and iterate through all of them 
    for data in re.finditer(r'\?',puzzle):
        # if the question mark is at the start of the string puzzle exclude only the character following it
        if data.span()[0] == 0: 
            excludeChar = puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # if the question mark is at the end of the string puzzle exclude only the character preceding it
        elif data.span()[1] == len(puzzle):
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)]
        # else exclude characters on both the sides of question mark
        else:
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)] + puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # substitute each question mark one by one with random choice of lowercase characters excluding the exclude character
        puzzle= re.sub(r'\?',random.choice([i for i in string.ascii_lowercase if i not in excludeChar]),puzzle,count=1)
    return puzzle

# this is the driving code to test the three examples here 
print(replaceQuestionMark('xy?xz?'))
print(replaceQuestionMark('ab?e?mr??'))
print(replaceQuestionMark('??????'))