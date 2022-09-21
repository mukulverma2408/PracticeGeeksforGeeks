#Read text file into a variable and replace all newlines with space
with open("Samplefile.txt", 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)