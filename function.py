def countWordFromFile():
    fileName=input("enter the file name")
    words=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        words=words+len(words)
    print("numberbof words:")
    print(words)

countWordFromFile()