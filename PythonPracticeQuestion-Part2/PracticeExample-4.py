#Remove duplicate element from a list
import pandas as pd
def remove_dup(lst):
    df = pd.DataFrame(lst)
    df2 = df.value_counts()<=1
    print(df2)

l1 = [1,4,6,4,6,8,9,1,3,5]
remove_dup(l1)