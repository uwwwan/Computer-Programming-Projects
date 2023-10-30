for i in range(5):

    username = "rain"
    password = "rain"

    user = input("Enter your Username: ")
    passwrd = input("Enter your Password: ")

    if username == user and password == passwrd:
        print("Login Successful")
        break
    else:
        print("Login Failed, Try Again")



score = 30
counter = 0
questions1 = [
    ("1. A __ enables a particular set of conditions to be executed repeatedly until a condition is satisfied.\n",
     "for loop"),
    ("2. __ is executed when the loop has exhausted iterating the list.\n", "else statement"),
    ("3. __ generates a set of whole numbers starting from 0 to infinite\n", "range"),
    ("4. The __ is used exclusively for counting; that is to repeat a loop action as it either counts up or counts down\n", "for loop"),
    ("5. A python programming language allows using a loop inside another loop.\n", "nested loop"),
    ("6. Range(__) :generates a set of whole numbers starting from start to stop-1\n", "start, stop"),
    ("7. Range(__): The default step_size is 1 which is why when we didn't specify the step_size, the numbers generated are having a difference of 1.\n", "start, stop, step_size"),
    ("8. An alternative way of iterating through each item is by index offset into the sequence itself.\n", "sequence index"),
    ("9. If the __ is used with a while loop, the __ is executed when the condition becomes false.\n", "else statement"),
    ("10. Python supports having an __ statement associated with a loop statement.\n", "else statement"),
    ("11. Control Statements in a loop alter the execution sequence.\n", "true"),
    ("12. It is generally used to indicate pass or unimplemented functions and loops.\n", "false"),
    ("13. The continue statement allows you to bypass the current iteration of any loop.\n", "true"),
    ("14. The pass statement is used inside the loop to exit out of the loop.\n", "false"),
    ("15. The break statement is considered a no-operation statement, which means it consumes the execution cycle like a valid python statement.\n", "false"),
    ("16. The pass statement is much like a comment, but the python interpreter executes the pass statements like a valid python statement while it ignores the comment statement completely.\n", "true"),
    ("17. Whenever the controller encounters a break statement, it comes out of that loop immediately.\n", "true"),
    ("18. Python supporters these control statements. BREAK, CONTINUE, PASS, NULL.\n", "false"),
    ("19. Continue statement does not end the loop but rather moves on to the next iteration.\n", "true"),
    ("20. When execution exits a scope, not all automatic objects created in that scope are destroyed.\n", "false"),
    ("21. __ are used on conditional statements that yield a result of either a TRUE or FALSE value.\n", "logical operators"),
    ("22. The __ operators l determines whether two criteria are TRUE at the same time.\n", "and"),
    ("23. The __ operator returns TRUE when one or both of the conditions are met.\n", "or"),
    ("24. The __ operator is only valid for one condition.\n", "not"),
    ("25. Logical __ : True if either of the operands is true.\n", "or"),
    ("26. Logical__: True if the operand is false.", "not"),
    ("27. Logical__: True if both the operands are true.\n", "and"),
    ("28. True if either of the operands is true\n", "syntax x or y"),
    ("29. True if the operand is false.\n", "syntax not x"),
    ("30. True if both the operands are true.\n", "syntax x and y")

]

if username == user and password == passwrd:
    print("========== Identification M11 ==========")
    for question, correct_answer in questions1:
        answer = input(f"{question} Answer: ")
        counter += 1

        if answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"The answer is {correct_answer}")
            score -= 1
        if counter == 10:
            print()
            print("========== True Or False M12 ==========")
            print()
        if counter == 20:
            print()
            print("========== Identification M13 ==========")
            print()


if username == user and password == passwrd:
    ave = 30 / 3
    print(f"Score: {score}")
    print(f"Average: {ave}")
    if score >= 15 and score <= 20:
        print("You Passed, Well Done!")
    elif score >= 20 and score <= 25:
        print("You did great!")
    elif score == 30:
        print("Wow, Perfect!")
    elif score <=15:
        print("You did well!")
