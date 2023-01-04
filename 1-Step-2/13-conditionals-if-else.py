"""Conditionals : if - else  """

# if - else  conditionals example
def main():
    expected_answer = "50"
    user_input = input("What do you think the answer is? : ")
    
    if user_input == expected_answer:
        print("Welcome onboard.")
    else:
        print("Sorry try again!")

main()