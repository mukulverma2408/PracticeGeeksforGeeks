#How to count number of instances of a class in Python?
class sample:
    counter = 0
    def __init__(self):
        sample.counter += 1

s1 = sample()
s2 = sample()
s3 = sample()

print(sample.counter)