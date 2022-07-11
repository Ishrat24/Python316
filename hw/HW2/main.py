#Ishrat Amin

#Description :
# This code defines CFG.In this code our task is to add exponent to CFG.On line 14 i added an exponent operator which is '^' and then changed the sentence according to grammar.My output is shown on the right hand side of the IDE.

# In this code, i imported nltk library to draw the parse tree.

from nltk import CFG
import nltk

grammar = nltk.CFG.fromstring("""
S -> Expression
Expression -> Expression PlusMinus Term | Term
Term -> Factor | Term TimesDivide Factor
Factor -> 'X' | 'Y' | 'Z' | Factor Exponent Factor
Exponent -> '^'
PlusMinus -> '+' | '-'
TimesDivide -> '*' | '/'                  
""")

print('The productions are:', grammar.productions())

from nltk import ChartParser
parser = ChartParser(grammar)
sentence = 'X - Y / Y ^ Z'.split()
print('The statement is', sentence)
for tree in parser.parse(sentence):
    print(tree)
    tree.draw()