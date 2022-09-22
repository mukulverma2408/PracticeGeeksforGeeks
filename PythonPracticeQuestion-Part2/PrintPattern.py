#Print the number pattern
counter = 1
for i in range(5, 0, -1):
    print(' '.join(str(counter)*i))
    counter +=1
