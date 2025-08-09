
secret_word = "abbas"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("enter your guess:")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("you guessed too high")
else:
      print("you guessed correctly")
