
def translate(phrase):
    translator = ""
    for char in phrase:
        if char.lower() in " aeiou":
            if char.isupper():
                translator = translator + "G"
            else:
                translator = translator + "g"
        else:
            translator = translator + char
    return translator

print(translate(input("Enter a phrase: ")))