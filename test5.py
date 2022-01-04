# import requests
# import json
# r = requests.get("https://opentdb.com/api.php?amount=1")
# r.status_code
# r.headers
# question = json.loads(r.text)
# print(question)

import requests
import json
import pprint
import random
import html


url = "https://opentdb.com/api.php?amount=1"
endGame = ""

score_correct = 0
score_incorrect = 0

while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game.")
    else:
        data = json.loads(r.text)
        # pprint.pprint(data)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        # random.shuffle(answers)
        valid_answer = False
        answer_number = 1
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\nType the number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid Answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers.")

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            score_correct += 1

            print("\nCongratulations! You answered correctly! The correct answer was: " + html.unescape(correct_answer))
        else:
            score_incorrect += 1

            print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + html.unescape(correct_answer))

        print("Your score is:")
        print("Correct answers: " + str(score_correct))
        print("Incorrect answers: " + str(score_incorrect))

        endGame = input("\nPress enter to play again or type 'quit' to quit the game.").lower()

print("\nThanks for playing")
