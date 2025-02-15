import os
os.system("clear")
print('''hi my name is parick
i like hack but i cant
zdereg creat me for help people''')
import json
from difflib import get_close_matches

#Load Data
def load_data(filePath : str):
    with open(filePath , 'r') as dataFile:
        data = json.load(dataFile)
    return data

#Save Data
def save_data(filePath : str , data : dict):
    with open(filePath , 'w') as dataFile:
        json.dump(data , dataFile , indent=2)

#Find The Best Match
def find_best_question(userQuestion : str , questions : list[str]):
    matches = get_close_matches(userQuestion , questions , n=1 , cutoff=0.6)
    return matches[0] if matches else None

#Load Answer
def find_best_answer(question : str , data : dict):
    for q in data["questions"]:
        if q["question"] == question:
            return q["answer"]

#Start
def chatBot():
    data = load_data('data.json')

    while True:
        userInput = input("You: ").lower()
        if userInput == "quit":
            break

        bestMatch = find_best_question(userInput , [q["question"] for q in data["questions"]])

        if bestMatch:
            answer = find_best_answer(bestMatch , data)
            print(f"Bot: {answer}")
        else:
            print("I don't the answer, Can you teach me?")
            newAnswer = input("Type the answer or 'Skip' to skip: ").lower()
            if newAnswer != "skip":
                newData = {"question": userInput , "answer": newAnswer}
                data["questions"].append(newData)
                save_data('data.json' , data)
                print("Bot: Thank you! I learned a new response.")

if __name__ == "__main__":
    chatBot()
