myFile = open("new.txt", "w+")
while True:
    try:
        st = input()
    except EOFError:
        break
    myFile.write(st + '\n')
    myFile.close()
