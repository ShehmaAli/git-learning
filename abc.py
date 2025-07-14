quiz = {
    "what is the colour of the sky? ": "blue",
    "how many planets are there in our solar system? ": "8",
    "Who played the iron man in the avengers endgame? ": "robert downey junior"
}
"""
git remote
git commit ✔️
git branch
git checkout
git pull ✔️
git push ✔️test change

"""
answers = []
name = input("What is your name? ")
decision = input("Do you want answer some questions? (y for yes & n for no) ")

if decision == "y":
    print(f"hello {name}")
    for q in quiz.keys():
        answer = input(q)
        answers.append(answer)
if answers == list(quiz.values()):
    print("yes")
else:
    print("no")
