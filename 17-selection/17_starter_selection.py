# Macrolab 1.7 / Decision-based project

# In this macrolab, you will apply your understanding of selection in Python to build a small program that makes decisions.

# Project: 10-question quiz

# Instructions:
# - Write a Python program that asks the user 10 quiz questions.
# - After each answer, give immediate feedback (correct / incorrect).
# - Keep track of the score as the user progresses.
# - At the end, display the total score out of 10.
# - Use if, if-else, or elif statements to check answers.
# - Make sure to handle input carefully (e.g., case sensitivity, expected answer format).

# Example structure:
# question = "What is the capital of France?"
# answer = input(question + " ")
# if answer.lower() == "paris":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect.")

# You can store questions in a list or just write them one by one.

def main():
    score = 0

    # Example question 1 (you will write 10 total)
    question1 = "What is the capital of France? "
    answer1 = input(question1)
    if answer1.lower() == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    # Add 9 more questions following the same pattern!

    # At the end, print the total score
    print(f"Your final score is {score} out of 10.")

if __name__ == "__main__":
    main()

# Remember to:
# - Add meaningful comments to your code
# - Check for input consistency (e.g., lower() or strip())
# - Test your code to ensure it works as expected
# - Save and push your completed file to GitHub under /1.7-selection/macrolab/
