secret_word = "giraffe"

guess = ""
count = 0
guess_limits = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count < guess_limits:
        guess = input("Enter the secret word:")
        count = count + 1
        print("You have counted "+ str(count) + " times.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")