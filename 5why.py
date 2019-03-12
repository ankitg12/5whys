#initialq = raw_input("What do you want to resolve?")
answers=[]
ans = raw_input("What is happening ? ")
answers.append(ans)
try:
    while True:
        ans = raw_input("Why " + ans + "? ")
        answers.append(ans)
except KeyboardInterrupt:
    answers.append("\n")
    print answers

with open('answers.txt','a') as outfile:
    outfile.write("\n".join(answers))
