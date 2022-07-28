#Progg to print Even number between 1 to 10
def display_even_number(n):
    counter = 0
    for i in range(1, n):
        if i % 2 == 0:
            counter += 1
            print(i)
    print("We have {} even number".format(counter))

display_even_number(10)
