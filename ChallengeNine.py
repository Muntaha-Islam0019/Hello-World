# You'll have a car. The user can tell you to start, stop and quit the
# program. Help keyword will help user to understand the commands.

key = ''
print("Enter 'help' for help.")
isStarted = False

while True:

    key = input("Your Command: ")

    if key == 'help':
        print('''
Commands:
         
start - starts the car 🚗,
stop - stops the car 🚧,
quit - quits the game 👋🏻.
           
Enjoy!
         ''')
    elif key == 'start' and not isStarted:
        isStarted = True
        print('Car started! 🚗')
    elif key == 'start' and isStarted:
        print('Car already started.')
    elif key == 'stop' and isStarted:
        isStarted = False
        print('Car stopped! 🚧')
    elif key == 'stop' and not isStarted:
        print("Car isn't moving.")
    elif key == 'quit':
        break
    else:
        print("Hey, I don't understand what you're saying 😥")

isStarted = False
print('Game closed. 👋🏻')
