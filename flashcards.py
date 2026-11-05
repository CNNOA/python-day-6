# quit_app
# get_random_question
# show_question 
# show_answer


flashcard = [
    {"question" : "what Python keyword is used to define a function?", "answer" : "def"},
    {"question" : "what Python data type represesnt WHOLE number?", "answer" : "int"},
    {"question" : "what data structure is used to represnt key, value pairs?", "answer" : "dictionary"},
]

'''
Task: Tell the user googbye.
Input: None
Side Effect: Prints a goodbye message to Terminal
Retrun: None
'''
def quit_app():
    print("Thanks for studying, come back soon!")

'''
Task: Selects and Retrieves a Random Elements in the Flashcards list
Input: Flashcards list
Side Effect: None
Retrun: the Flashcard(dictionary)
'''
def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card


'''
Task: Display the question.
Input: Question Card
Side Effect: Print the question text to Terminal.
Retrun: None
'''
def show_question(card):
    question = card["question"]
    print("Question:", question)

'''
Task: Display the answer.
Input: Question card.
Side Effect: Print the answer text to Terminal.
Retrun: one
'''
def show_answer():
    answer = card["answer"]
    print("Answer:", answer)

def main():
    
    """
    Task: Run the flashcard program.
    Input: A list of flashcards.
    Side Effect: Displays cards and prompts the user.
    Return: None
    """
    whlie Ture:
        chosen_card = get_random_question(flashcard)
        show_question(chosen_card)

        user_choice = input("Enter Q to quit,type anything else to continue.").lower().strip

        if user_choice == "q":
            quit_app()
            break

        else:
            show_answer(chosen_card)


main()