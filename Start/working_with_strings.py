print("Superz\nAcademy")
#/n creates a new line in a single string
print("Superz\"Academy\"")
#to use '"' in string add '\' before it
phrase = "Superz Academy"
print(phrase.isupper())
#use .upper or .lower to convert, .islower or .isupper to get true or false value
print(phrase.lower().islower())

print(len(phrase))
#len() tells no. of character in a string

print(phrase[0])
#use [] after a variable to get a character in a string(first character starts from 0)

print(phrase.index("Superz"))
# .index() gives the no. at which a word or a character starts from

print(phrase.replace("Superz","Abbas"))