#Write Prog to place 0 at end
#[1,4,6,0,6,0,4,5,7,0]
def move_zero(lst):
    newlst = []
    zerolst = []
    for i in lst:
        #print(i)
        if i == 0:
            zerolst.append(0)
        else:
            newlst.append(i)
        #print(zerolst)
        #print(newlst)
    newlst.extend(zerolst)
    return(newlst)

l1 = [1,4,6,0,6,0,4,5,7,0]
print(move_zero(l1))

