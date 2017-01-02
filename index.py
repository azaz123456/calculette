#####################################################################
#@ calculatrice
#@ 02-01-2016
#@ iseba
#####################################################################
# Module Import

# function and variables creation

# body script
int1 = eval(raw_input("entre un int1 --> "))
int2 = eval(raw_input("entre un int2 --> "))
operateur = raw_input("entre un operateur --> ")
lol = 0

if operateur == "+":
    lol = int1 + int2
elif operateur == "-":
    lol = int1 - int2
elif operateur =="/":
    lol = int1 / int2

print lol