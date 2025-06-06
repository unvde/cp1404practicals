"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: This line ensures the loop will exit when a valid integer is entered.
    except ValueError:  # TODO - Catch the ValueError exception that occurs when the input is not an integer.
        print("Please enter a valid integer.")
print("Valid result is:", result)
