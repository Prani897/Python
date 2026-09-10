user_input=""

while True:
    user_input=input("").lower()
    
    if user_input == "start":
        print("Car Started... Ready tp gp!")
    elif user_input == "stop":
        print("Car Stopped.")
    elif user_input == "help":
        print('''
            start - to start the car
            stop - to stop the car
            quit - to exit
           ''')
    elif user_input == "quit":
        break
    else:
        print("I Don't understand thta....")
      