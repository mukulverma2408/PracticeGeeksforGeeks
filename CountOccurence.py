#Progg to count occurence of an element in list

def count_occur(lst, item):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == item:
            counter +=1
    print("{} occured {} times".format(item, counter))

lst = [1,3,5,6,3,1,6,7,9,3,2,4,3,3]
count_occur(lst, 6)
