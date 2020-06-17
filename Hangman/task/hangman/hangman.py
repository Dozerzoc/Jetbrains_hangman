import random


while True:
    question = input("Type \"play\" to play the game, \"exit\" to quit:")
    if question == "exit":
        break
    elif question == "play":
        print("H A N G M A N")

        def is_ascii(s):
            return all(ord(c) < 128 for c in s)

        given_list = ['python', 'java', 'kotlin', 'javascript']
        answer = random.choice(given_list)
        answer_list = list(answer)
        hidden_list = list(len(answer) * '-')
        output = len(answer) * '-'
        counter = 0
        check_list = []

        while counter < 8:
            print()
            print(output)
            if output == answer:
                print("You guessed the word!")
                print("You survived!")
                break
            letter = input("Input a letter:")
            if letter in answer and letter.islower():
                if letter not in hidden_list:
                    check_list.append(letter)
                    position = [p for p, x in enumerate(answer) if x == letter]
                    for p in position:
                        if letter == answer_list[p]:
                            hidden_list[p] = letter
                            output = "".join(hidden_list)
                else:
                    print("You already typed this letter")
            else:
                if len(letter) != 1:
                    print('You should input a single letter')
                elif not letter.islower() or not is_ascii(letter):
                    print('It is not an ASCII lowercase letter')
                else:
                    if letter in tuple(check_list):
                        print("You already typed this letter")
                    else:
                        print("No such letter in the word")
                        counter += 1
                        check_list.append(letter)
        if output != answer:
            print("You are hanged!")
        pass

