score = 15
counter = 0
QUESTIONS = [
    ("1. It enables a particular set of conditions to be executed repeatedly until a condition is satisfied?\n", "for loop"),
    ("2. A function that either take a single number and behaves like a list?\n", "range"),
    ("3. The statement used inside the loop to exit out of the loop?\n", "break statement"),
    ("4. It is a declaration that enables you to ignore the most recent version of any loop?\n", "continue statement"),
    ("5. The statement that is considered a no-operation statement?\n", "pass statement"),
    ("6. Loop Controls Statements Control statements in a loop change the order of execution.\n", "false"),
    ("7. The Continue Statement is used within the loop to exit the loop.\n", "false"),
    ("8. The Pass Statement is regarded as a no-operation statement, says that it consumes the execution cycle like a legal Python statement, but nothing actually happens. When the command pass is executed.\n", "true"),
    ("9. WHILE LOOP enables a specific set of conditions to be repeated until a criterion has been met.\n", "false"),
    ("10. Iterating by sequence index enables a specific set of conditions to be repeated until a criterion has been met.\n", "true"),
    ("11. The continue statement inserted inside the loop to end it.\n", "false"),
    ("12. Python programming language allows using one loop inside another loop is called nested loop.\n", "true"),
    ("13. While Loop is used for sequential traversal.\n", "false"),
    ("14. Brake statement is useful when we want to terminate the loop as soon the condition is fulfilled instead of doing the remaining iterations.\n", "false"),
    ("15. Python does not support having an else statement associated with a loop statement.\n", "false")


]
print("\033[32mIDENTIFICATION\033[0m")
for question, correct_answer in QUESTIONS:
    answer = input(f"{question} \033[34mANSWER: \033[0m")
    counter +=1
    
    if answer.lower() == correct_answer:
        print("\033[33mCorrect!\033[0m")
    else:
        print(f"\033[31mThe answer is {correct_answer}, not {answer}\033[0m")
        score -=1
    if counter == 5:
        print("\033[32mTRUE OR FALSE\033[0m")

print(f"SCORE: {score}")