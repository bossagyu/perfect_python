done = False
while not done:
    echo_text = raw_input("echo > ")
    if echo_text == "bye":
        done = True
        print("good by")
    elif echo_text == 'done':
        done = True
    else:
        print(echo_text) 
