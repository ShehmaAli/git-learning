a = 10
b = 20
c = a + b

d = 20 // 3

"""
git remote
git commit ✔️
git branch ✔️
git checkout ✔️
git pull ✔️
git push ✔️
"""

print(a, b, c, d)

"""
quiz = {
    "What is the colour of the sky? ": "blue",
    "How many planets are there in our solar system? ": "8",
    "Who played Iron Man in Avengers: Endgame? ": "Robert Downey Jr"
}
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
"""

user_num = int(input("Please enter a number: "))

for star_num in range(user_num + 1):
    print('*' * star_num)