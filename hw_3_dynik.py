list_of_commands = []

while True:
    command = input('Введіть команду:').lower()
    if command == 'add':
        list_of_commands.append(input('Введіть нотатку:').lower())  # Add notes to the list
    elif command == 'earliest':
        print(f'Від найстарішої до найновішої: {list_of_commands}')  # Print earliest notes
    elif command == 'latest':
        print(f'Від найновішої до найстарішої:{list_of_commands[::-1]}')  # Print latest notes
    elif command == 'longest':
        print(f'Від найдовшої до найкоротшої:{sorted(list_of_commands, key=len, reverse=True)}')
        # Print longest notes first
    elif command == 'shortest':
        print(f'Від найкоротшої до найдовшої:{sorted(list_of_commands, key=len)}')  # Print shortest notes first
    elif command == 'exit':
        break  # Exit from program
    else:
        command = input('Введіть одну з існуючих команд:').lower()  # Validation if command is not present
