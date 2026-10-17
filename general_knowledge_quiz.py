
print("===================================")
print(" Welcome to the General Knowledge Quiz!")
print("===================================")
print("Answer all 3 questions.")
print()

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

print()

# Question 2
answer = input("2. How many days are there in a week? ").strip().lower()

if answer == "7" or answer == "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 7.")

print()

# Question 3
answer = input("3. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Mars.")

print()
print("===================================")
print(f"Your final score is {score}/3.")
print("Thank you for playing!")
print("===================================")
