def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yay or N for nej')
    return answer

response = get_yes_or_no('Do you like the beach? (Y)ay eller (N)ej:')
if response == 'Y':
    print('Great! Mr. Niceguy lives down by da beach.')
else:
    print("Too bad. You're missing out.")
