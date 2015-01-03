
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

for i in range(10):
    print i


for i in range(3,10):
    print i

for i in range(0,10):
    print i

while False:
    print("False")
else:
    print("done")


