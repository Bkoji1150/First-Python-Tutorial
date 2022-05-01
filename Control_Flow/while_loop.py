# WRite a progrand that would run until user hit quit

command = ""
while command.lower() != "quit":
    command = input("#: ")
    print("ECHO", command)