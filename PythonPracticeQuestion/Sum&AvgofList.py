#Find Sum and Average of element in list
def SumAvg(lst):
    lst_sum = sum(lst)
    lst_avg = lst_sum/len(lst)
    print("Sum is {} and Average is {}".format(lst_sum, lst_avg))

lst = [1,2,3,4,5,6]
SumAvg(lst)
