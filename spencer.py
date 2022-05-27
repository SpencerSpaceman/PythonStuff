from random import randint

num1 = randint(1,100)
num2 = randint(1,100)

question = "What is " + str(num1) + " plus " + str(num2) + "? "
user_answer = int(input(question))
correct_answer = num1 + num2

if user_answer == correct_answer:
        print("Thats right, well done")
else:
        print("No, im afraid the answer is " + str(correct_answer)+ ".")
