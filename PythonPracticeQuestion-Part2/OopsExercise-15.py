#What is a clean, Pythonic way to have multiple constructors in Python

class Sample:
    def __init__(self, ans):
        self.ans = ans

    @classmethod
    def twoargument(cls, args):
        op_two_args = (args[0] + args[1])
        return cls(op_two_args)

    @classmethod
    def threearguments(cls, args):
        op_three_args = (args[0]* args[1] * args[2])
        return cls(op_three_args)

lst = [[1,2], [1,2,3]]
for i in lst:
    if len(i) == 2:
        obj = Sample.twoargument(i)
        print(obj.ans)

    elif len(i) == 3:
        obj = Sample.threearguments(i)
        print(obj.ans)