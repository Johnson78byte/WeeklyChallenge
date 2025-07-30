quiz = [{
    "question" : "What is the Most popular football club in the World?",
    "options" : ["a. Manchester United", "b. Real Madrid", "c. Barcelona", "d. Newcastle United"],
    "answer": "b"
},
{
    "question" : "What is the most hated football club in the world?",
    "options": ["a. Liverpool","b. Arsenal", "c. Tottenham Hotspurs", "d. Manchester City"],
    "answer" : "a"
}, {
    "question": "Who is the scored most freeckicks in football history?",
    "options" : ["a. Lionel Messi", "b. Cristiano Ronaldo", "c. David Beckham", "d. Juninho Pernambucano"],
    "answer": "d"
}
]
def start_quiz():
    score = 0
    for a in quiz:
        print(a["question"])
        for opt in a["options"]:
         print(opt)
        answer = input("Enter your answer(a/b/c/d):").lower()
        if answer == a["answer"]:
            print("You got it right!")
            score += 1
        else:
            print(f"Wrong answer! Loser! The correct answer was: {a['answer']}")
    print(f"Your final score is {score} out of {len(quiz)}")

    if score == len(quiz):
        print("You are a genius!")
    elif score >= len(quiz) / 2:
        print("Not bad! You passed!")
    else:
        print("You know nothing about football man! You need to watch more football!")  

def main():
    while True:
        start_quiz()
        playagain = input("Do you want to try your luck again? (yes/no):").lower()
        if playagain != "yes":
            print("Go home loser!")
            break      

main()        
