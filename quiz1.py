
users = []
pwd = {}
n=1

print("Registration")
for i in range(n):
    username=input("enter username: ")
    password=input("enter password: ")
    users.append(username)
    key=username
    value=password
    pwd[key]=value
print("registration completed!")


print("LOGIN")
user1=input("enter username: ")
if user1!=username :
    print("Enter corrct username:")
    user1=input()
    
if user1 in users:
    pwd1=input("enter password: ")
    if pwd1 == pwd[user1]:
        print("LOGGED IN")
    else:
        print("wrong password")
        print("login again")
        for i in range(3):
            pwd1=input("enter password: ")
            if pwd1==pwd[user1]:
                print("LOGGED IN")
                break
            else:
                print("wrong password")
                continue

# filename = 'questions.txt'
# def loading(filename):
#     questions = []
    
#     try:   
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for i in range(0, len(lines)-1, 2):
#                 question = lines[i].strip()
#                 answer = lines[i + 1].strip()
#                 questions.append((question, answer))
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return None

#     return questions

# def askingquestion(question, correct_ans):
#     print(question)
#     user_answer = input("Your answer: ").strip().lower()
#     if user_answer == correct_ans.lower():
#         print("Correct!")
#         return True
#     else:
#         print(f"Wrong! The correct answer is: {correct_ans}")
#         return False


# def play(questions):
#     score = 0
#     for question, correct_ans in questions:
#         if askingquestion(question, correct_ans):
#             score += 1
#     print(f"\nGame Over! Your score: {score}/{len(questions)}") 


# def main():
#     questions = loading(filename)

#     if not questions: 
#         print("No questions available. Exiting the quiz.")
#         return
    
#     print("Welcome to the Quiz!\n")
#     play(questions)

# main()
