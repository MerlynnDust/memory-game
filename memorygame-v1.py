import time
import random

f = open("Text-File", "r")
content = f.read()

#TODO delete
test_paragraph = "This is a test paragraph"

def grab_a_sentence(text):
    listedText = content.split(".")
    listedTextLength = len(listedText)
    #set to global because printing is more important than returning for the sake of the test
    global grabbedSentence
    grabbedSentence = listedText[random.randint(0,listedTextLength)]
    print(grabbedSentence)
def wait_and_clearscreen(timeVar):
    time.sleep(timeVar)
    print(chr(27) + "[2J")


def test_user(test_sentence):
    user_input = input("Please try and recall what you just read:")

    #make them both comparable
    list_user_input = user_input.split()
    test_sentence = test_sentence.split()
    print(user_input)
    for i in range(len(test_sentence)):
        if list_user_input[i] != test_sentence[i]:
            print("You failed at word" + str(i + 1))
            break




grab_a_sentence(content)
wait_and_clearscreen(10)
test_user(grabbedSentence)




