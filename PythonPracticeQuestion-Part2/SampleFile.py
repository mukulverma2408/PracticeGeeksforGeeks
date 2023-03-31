import pandas as pd
df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']},
                  columns=['numbers', 'colors'])
print(df)

print(df.iloc[[0,2],[0,1]])


"""
def solution(S):
    occurrences = [0] * 26
    print(occurrences)

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
        print('Inside first if')
        print(occurrences)

    best_char = ''
    best_res = 0

    for i in range(0, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            print(best_char)
            best_res = occurrences[int(best_char)]

    return best_char
S = 'mukuisabla'
print(solution(S))
"""
