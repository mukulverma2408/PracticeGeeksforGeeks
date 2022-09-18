#Write a Python program to compute the edit distance between two given strings

def EditDistance(word1, word2):
    distance = 0
    refstr = ""
    len1, len2 = len(word1), len(word2)
    distance += abs(len1-len2)
    if len1 > len2:
        refstr = word2
    else:
        refstr = word1

    for i in range(len(refstr)):
        if word1[i] != word2[i]:
            distance += 1
    print("Distance b/w {} and {} is {}".format(word1, word2, distance))

EditDistance("kitten", "sitting")
EditDistance("medium", "median")